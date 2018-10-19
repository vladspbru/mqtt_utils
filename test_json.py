#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys

import yaql
import json
# import objectpath

txt = '{"Time":"2018-10-15T10:47:38","DS18B20-1":{"Id":"04173329BEFF","Temperature":17.2},"DS18B20-2":{"Id":"041752D93BFF","Temperature":24.3},"TempUnit":"C"}'

# from collections import namedtuple
# def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
# def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
# o = json2obj(txt)
# print(str(o))

def json_parse():
    data_source = json.loads(txt)
    print(str(data_source))

    engine = yaql.factory.YaqlFactory().create()
    expression = engine('$["DS18B20-1"]["Temperature"]')
    val = expression.evaluate(data=data_source)
    print(str(val))

    # jsonnn_tree = objectpath.Tree(data_source)
    # result = list(jsonnn_tree.execute('$..Temperature'))
    # print(str(result))




if __name__ == '__main__':
    try:
        print('-----------------------------------------------')
        json_parse()
        # main()
    except (SystemExit, KeyboardInterrupt):
        print('-----------------------------------------------')
    except:
        type, value, traceback = sys.exc_info()
        print("Exception: {}".format(value))
