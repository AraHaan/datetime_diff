# Some simple testing tasks (sorry, UNIX only).

.install-deps: requirements-dev.txt
	@pip install -U -r requirements-dev.txt
	@touch .install-deps

isort:
	isort -rc datetime_diff
	isort -rc tests

flake: .flake

.flake: .install-deps $(shell find datetime_diff -type f) \
                      $(shell find tests -type f)
	@flake8 datetime_diff
	@if python -c "import sys; sys.exit(sys.version_info < (3,5))"; then \
	    flake8 examples tests demos && \
            python setup.py check -rms; \
	fi
	@if ! isort -c -rc datetime_diff tests; then \
            echo "Import sort errors, run 'make isort' to fix them!!!"; \
            isort --diff -rc datetime_diff tests; \
            false; \
	fi
	@touch .flake


.develop: .install-deps $(shell find datetime_diff -type f) .flake
	@pip install -e .
	@touch .develop

test: .develop
	@py.test -q ./tests

vtest: .develop
	@py.test -s -v ./tests

cov cover coverage:
	tox

# cov-dev: .develop
#	@echo "Run without extensions"
#	@AIOHTTP_NO_EXTENSIONS=1 py.test --cov=datetime_diff tests
#	@py.test --cov=datetime_diff --cov-report=term --cov-report=html --cov-append tests
 #       @echo "open file://`pwd`/coverage/index.html"

cov-dev-full: .develop
	@py.test --cov=datetime_diff --cov-report=term --cov-report=html --cov-append tests
	@echo "open file://`pwd`/coverage/index.html"

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -f .coverage
	@rm -rf coverage
	@rm -rf build
	@rm -rf cover
#	@make -C docs clean
	@python setup.py clean
	@rm -f datetime_diff/__init__.html
	@rm -rf .tox

#doc:
#	@make -C docs html SPHINXOPTS="-W -E"
#	@echo "open file://`pwd`/docs/_build/html/index.html"

#doc-spelling:
#	@make -C docs spelling SPHINXOPTS="-W -E"

install:
	@pip install -U pip
	@pip install -Ur requirements-dev.txt

#.PHONY: all build flake test vtest cov clean doc
.PHONY: all build flake test vtest cov clean
