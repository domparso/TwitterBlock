#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


import os
import json
from datetime import datetime, date

def readJsonFile(jsonPath):

    if not os.path.exists(jsonPath):
        return False

    with open(jsonPath, 'r') as f:
        tmp = f.read().encode("utf-8")

        try:
            return json.loads(tmp)
        except Exception as e:
            print("json文件解析错误: ", e)
            return False

def writeJsonFile(jsonPath, p0):
    try:
        tmp = json.dumps(p0)
    except Exception as e:
        print("json对象反序列错误: ", e)
        return False

    with open(jsonPath, 'w') as f:
        f.write(tmp)
    return True


class DateEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

class NewEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        else:
            return json.JSONEncoder.default(self, obj)