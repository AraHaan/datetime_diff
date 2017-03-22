# coding=utf-8
"""
datetime_diff
~~~~~~~~~~~~~~~~~~~

Extension to the datetime module

:copyright: (c) 2017 Decorater
:license: MIT, see LICENSE for more details.

"""

__title__ = 'datetime_diff'
__author__ = 'Decorater'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017 Decorater'
__version__ = '0.0.1'
__build__ = 0x000001


def datetime_diff(datetime_prior, datetime_current):
    """
    Compares two different datetime objects
    and returns the time elapsed since.

    for example, a datetime object when turned
    into a string (being 2015-12-03 03:34:57.281000)
    when compared with a new datetime object
    (equivalent to the current time) one can determine
    how many years, months, days, hours, minutes, and
    seconds ago the prior datetime object was.
    This returns the data as a string readable by humans
    denoting how much time has passed since the specified
    prior datetime object.
    """
    elyear = datetime_current.year - datetime_prior.year
    elmonth = datetime_current.month - datetime_prior.month
    elday = datetime_current.day - datetime_prior.day
    elhour = datetime_current.hour - datetime_prior.hour
    elminute = datetime_current.minute - datetime_prior.minute
    elsecond = datetime_current.second - datetime_prior.second
    total_seconds = int((datetime_current - datetime_prior).total_seconds())
    if 0 < total_seconds < 60:
        # lets set things to the correct values now.
        elyear = 0
        elmonth = 0
        elday = 0
        elhour = 0
        elminute = 0
        elsecond = total_seconds
    reply = ""
    if elyear > 0:
        if elyear < 2:
            reply += "{0} year".format(elyear)
        else:
            reply += "{0} years".format(elyear)
    if elmonth > 0:
        if elyear > 0:
            reply += ", "
        if elmonth < 2:
            reply += "{0} month".format(elmonth)
        else:
            reply += "{0} months".format(elmonth)
    if elday > 0:
        if elyear > 0:
            reply += ", "
        elif elmonth > 0:
            reply += ", "
        if elday < 2:
            reply += "{0} day".format(elday)
        else:
            reply += "{0} days".format(elday)
    if elhour > 0:
        if elyear > 0:
            reply += ", "
        elif elmonth > 0:
            reply += ", "
        elif elday > 0:
            reply += ", "
        if elhour < 2:
            reply += "{0} hour".format(elhour)
        else:
            reply += "{0} hours".format(elhour)
    if elminute > 0:
        if elyear > 0:
            reply += ", "
        elif elmonth > 0:
            reply += ", "
        elif elday > 0:
            reply += ", "
        elif elhour > 0:
            reply += ", "
        if elminute < 2:
            reply += "{0} minute".format(elminute)
        else:
            reply += "{0} minutes".format(elminute)
    if elsecond > 0:
        if elyear > 0:
            reply += ", "
        elif elmonth > 0:
            reply += ", "
        elif elday > 0:
            reply += ", "
        elif elhour > 0:
            reply += ", "
        elif elminute > 0:
            reply += ", "
        if elsecond < 2:
            reply += "{0} second".format(elsecond)
        else:
            reply += "{0} seconds".format(elsecond)
    if elyear or elmonth or elday or elhour or elminute or elsecond > 0:
        reply += " ago."
    return reply
