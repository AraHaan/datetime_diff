# coding=utf-8
"""
tests datetime_diff package.
"""
import datetime
import time

import datetime_diff


def test_years():
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year - 1, 12, 3, 3, 34, 57, 281000)
    assert datetime_diff.datetime_diff(olddate, now) == "1 year ago."


def test_multiple_years():
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year - 2, 12, 3, 3, 34, 57, 281000)
    assert datetime_diff.datetime_diff(olddate, now)  == "2 years ago."


def test_months():
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month - 1, now.day, now.hour, now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 month ago."


def test_multiple_months():
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month - 2, now.day, now.hour, now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now)  == "2 months ago."


def test_datetime_diff():
    oldnow = datetime.datetime.now()
    time.sleep(15)
    newnow = datetime.datetime.now()
    assert datetime_diff.datetime_diff(oldnow, newnow) == "15 seconds ago."
