# coding=utf8

import json
from datetime import date, datetime


class ValueFormatError(Exception):
    pass


def __default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    else:
        raise TypeError('%r is not JSON serializable' % obj)


def to_str(data):
    if isinstance(data, (dict, list, tuple)):
        return json.dumps(data, default=__default)
    elif isinstance(data, Exception):
        return data.message
    elif isinstance(data, basestring):
        return data
    elif isinstance(data, (int, float, bool)):
        return str(data)
    else:
        raise ValueFormatError("不支持的日志数据类型", data)
