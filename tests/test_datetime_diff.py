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
    datetime_diff.datetime_diff(olddate, newnow)


def test_multiple_years():
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year - 2, 12, 3, 3, 34, 57, 281000)
    datetime_diff.datetime_diff(olddate, newnow)


def test_datetime_diff():
    oldnow = datetime.datetime.now()
    time.sleep(15)
    newnow = datetime.datetime.now()
    assert datetime_diff.datetime_diff(oldnow, newnow) == "15 seconds ago."
