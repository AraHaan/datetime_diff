# coding=utf-8
"""
tests datetime_diff package.
"""
import datetime
import time

import datetime_diff


def test_years():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year - 1, now.month, now.day, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 year ago."


def test_multiple_years():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year - 2, now.month, now.day, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "2 years ago."


def test_months():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month - 1, now.day, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 month ago."


def test_multiple_months():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month - 2, now.day, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "2 months ago."


def test_days():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day - 1, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 day ago."


def test_multiple_days():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day - 2, now.hour,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "2 days ago."


def test_hours():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour - 1,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 hour ago."


def test_multiple_hours():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour - 2,
                                now.minute, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "2 hours ago."


def test_minutes():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour,
                                now.minute - 1, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "1 minute ago."


def test_multiple_minutes():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour,
                                now.minute - 2, now.second)
    assert datetime_diff.datetime_diff(olddate, now) == "2 minutes ago."


def test_seconds():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour,
                                now.minute, now.second - 1)
    assert datetime_diff.datetime_diff(olddate, now) == "1 second ago."


def test_multiple_seconds():
    """test for datetime_diff."""
    now = datetime.datetime.now()
    olddate = datetime.datetime(now.year, now.month, now.day, now.hour,
                                now.minute, now.second -2)
    assert datetime_diff.datetime_diff(olddate, now) == "2 seconds ago."


def test_datetime_diff():
    """test for datetime_diff."""
    oldnow = datetime.datetime.now()
    time.sleep(15)
    newnow = datetime.datetime.now()
    assert datetime_diff.datetime_diff(oldnow, newnow) == "15 seconds ago."
