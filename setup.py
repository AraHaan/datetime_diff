from setuptools import setup
from setuptools.command.test import test as TestCommand

requirements = []

version = '0.0.1'

if not version:
    raise RuntimeError('version is not set')

try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ""


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)

setup(name='datetime_diff',
      author='Decorater',
      author_email='seandhunt_7@yahoo.com',
      url='https://github.com/AraHaan/datetime_diff',
      bugtrack_url='https://github.com/AraHaan/datetime_diff/issues',
      version=version,
      packages=['datetime_diff'],
      license='MIT',
      description='Extension to the datetime module',
      long_description=readme,
      maintainer_email='seandhunt_7@yahoo.com',
      download_url='https://github.com/AraHaan/datetime_diff',
      include_package_data=True,
      install_requires=requirements,
      tests_require=['pytest', 'flake8', 'pyflakes', 'coverage',
                     'isort', 'pytest-cov', 'pytest-mock',
                     'pytest-timeout'],
      platforms='Any',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
      ],
      cmdclass=dict(test=PyTest)
)
