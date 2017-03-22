.. image:: https://travis-ci.org/AraHaan/datetime_diff.svg?branch=master
  :target: https://travis-ci.org/AraHaan/datetime_diff
.. image:: https://ci.appveyor.com/api/projects/status/vaxfcmgq0uusrkd4?svg=true
  :target: https://ci.appveyor.com/project/AraHaan/datetime-diff
.. image:: https://codecov.io/gh/AraHaan/datetime_diff/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/AraHaan/datetime_diff
.. image:: https://img.shields.io/pypi/v/datetime_diff.svg
   :target: https://pypi.python.org/pypi/datetime_diff/
.. image:: https://img.shields.io/pypi/pyversions/datetime_diff.svg
   :target: https://pypi.python.org/pypi/datetime_diff/

The ``datetime_diff`` package provides a useful function for comparing
two different datetime objects and returns the time elapsed since.

for example, a datetime object when turned into a string (being
2015-12-03 03:34:57.281000) when compared with a new datetime object
(equivalent to the current time) one can determine how many years,
months, days, hours, minutes, and seconds ago the prior datetime object
was.

This returns the data as a string readable by humans denoting how much
time has passed since the specified prior datetime object.

