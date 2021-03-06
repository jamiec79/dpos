# -*- coding: utf-8 -*-
# © Toons

"""
"""

from dposlib.blockchain import cfg
from datetime import datetime, timedelta

import pytz


def getTimestamp(**kw):
	"""
	return blockchain timestamp from datetime keyword arument.
	>>> getTimestamp(days=6, hours=4, minutes=20)
	"""
	delta = timedelta(**kw)
	return getTime(datetime.now(pytz.UTC) - delta)


def getTime(time=None):
	delta = (datetime.now(pytz.UTC) if not time else time) - cfg.begintime
	return delta.total_seconds()


def getRealTime(epoch=None):
	epoch = getTime() if epoch is None else epoch
	return cfg.begintime + timedelta(seconds=epoch)


def getSlot(epoch=None):
	epoch = getTime() if epoch is None else epoch
	return int(epoch // cfg.blocktime)


def getSlotTime(slot):
	return slot * cfg.blocktime


def getSlotRealTime(slot):
	return getRealTime(slot * cfg.blocktime)


def getLastSlot(slot):
	return slot + cfg.delegate
