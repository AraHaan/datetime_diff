from setuptools import setup

requirements = []

version = '0.0.1'

if not version:
    raise RuntimeError('version is not set')

try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ""

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
        'Topic :: Utilities',
      ]
)
