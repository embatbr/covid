# -*- coding: utf-8 -*-

from datetime import datetime as dt
from datetime import timedelta as td


def safe_int(x):
    if x and x.isdigit():
        return int(x)
    return None


def line2dict(obj):
    splitted_line = obj.split()

    def _get_word(i):
        if len(splitted_line) >= (i + 1):
            return splitted_line[i]
        return None

    return {
        'host': _get_word(0),
        'timestamp': {
            'time': _get_word(3)[1:] if _get_word(3) else None,
            'offset': _get_word(4)[:-1] if _get_word(4) else None
        },
        'verb': _get_word(5)[1:] if _get_word(5) else None,
        'endpoint': _get_word(6),
        'protocol': _get_word(7)[:-1] if _get_word(7) else None,
        'status': _get_word(8),
        'bytes': _get_word(9)
    }


def convert(obj):
    def _convert_timestamp(time_str):
        if not time_str:
            return None

        return dt.strptime(time_str, '%d/%b/%Y:%H:%M:%S')

    def _convert_timezone(raw_offset):
        if not raw_offset:
            return None

        raw_offset = int(raw_offset)

        return {
            'factor': -1 if raw_offset < 0 else 1,
            'hours': abs(raw_offset/100),
            'minutes': abs(raw_offset) - abs(raw_offset/100)*100
        }

    timestamp = _convert_timestamp(obj['timestamp']['time'])
    offset = _convert_timezone(obj['timestamp']['offset'])

    if timestamp and offset:
        timestamp = timestamp + td(hours=(offset['factor']*offset['hours']))
        timestamp = timestamp + td(minutes=(offset['factor']*offset['minutes']))

    return {
        'host': obj['host'],
        'timestamp': timestamp,
        'verb': obj['verb'],
        'endpoint': obj['endpoint'],
        'protocol': obj['protocol'],
        'status': safe_int(obj['status']),
        'bytes': safe_int(obj['bytes'])
    }


def question_1(rdd_param):
    rdd = rdd_param.map(lambda x: (x['host'], 1))
    rdd = rdd.filter(lambda x: x[0] is not None)
    rdd = rdd.reduceByKey(lambda x, y: x + y)
    rdd = rdd.map(lambda x: x[0])

    return rdd.collect()


def question_2(rdd_param):
    rdd = rdd_param.map(lambda x: x['status'])
    rdd = rdd.filter(lambda x: x is not None)
    rdd = rdd.filter(lambda x: x == 404)

    return rdd.count()


def question_3(rdd_param):
    rdd = rdd_param.filter(lambda x: x['status'] == 404)
    rdd = rdd.map(lambda x: (x['host'], 1))
    rdd = rdd.filter(lambda x: x[0] is not None)
    rdd = rdd.reduceByKey(lambda x, y: x + y)

    return rdd.top(5, key=lambda x: x[1])


def question_4(rdd_param):
    rdd = rdd_param.filter(lambda x: x['status'] == 404)
    rdd = rdd_param.map(lambda x: (x['timestamp'], 1))
    rdd = rdd.filter(lambda x: x[0] is not None)
    rdd = rdd.map(lambda x: (x[0].strftime('%Y-%m-%d'), x[1]))
    rdd = rdd.reduceByKey(lambda x, y: x + y)

    return rdd.collect()


def question_5(rdd_param):
    rdd = rdd_param.map(lambda x: x['bytes'])
    rdd = rdd.filter(lambda x: x)

    return rdd.reduce(lambda x, y: x + y)


questions = {
    1: question_1,
    2: question_2,
    3: question_3,
    4: question_4,
    5: question_5
}
