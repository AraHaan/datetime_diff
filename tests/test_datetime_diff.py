# coding=utf-8
"""
tests datetime_diff package.
"""
import datetime
import time

import datetime_diff


def test_datetime_diff():
    oldnow = datetime.datetime.now()
    time.sleep(15)
    newnow = datetime.datetime.now()
    assert datetime_diff.datetime_diff(oldnow, newnow) == "15 seconds ago."
