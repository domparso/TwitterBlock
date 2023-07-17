#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""

import os
import sys
import platform

# 软件版本信息
VERSION = "v0.0.1"
RUNTIMEENV = None
os_platform = platform.system()
ROOT_PATH, CONFIGFILE = os.path.split(sys.argv[0])

if getattr(sys, 'frozen', False):
    BUNDLE_DIR = sys._MEIPASS
    RUNTIMEENV = "pyinstaller"
else:
    BUNDLE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_PATH = os.path.join(BUNDLE_DIR, 'data')

# APPLICATION SERVER CONFIG FILES
CONFIGLIST = {
    "origin": 'cloud.superego.cyou',
    'ipaddr': '127.0.0.1',
    "server": {
        "id": 0,
        "port": 7080,
        "loglevel": 4
    },
    "pollingTime": 60
}

WEBSERVERCONFIG = {
    "protocol": 'http',
    "host": 'localhost',
    "port": '8080',
    "uri": '/api/v1'
}

#
HASH = {
    "aes": {
        "iv": '',
        "key": ''
    },
    "sha256": {
        "key": ''         # data sha256 key
    },
    "sha512": {
        "key": ''
    }
}

JOSE = {
    "jwt": {
        "key": '',
        "algorithm": 'HS256'
    },
    "jwe": {
        "key": '',
        "algorithm": 'dir',
        "encryption": 'A128CBC-HS256'
    }
}

# 允许跨域LIST
CORS_LIST = [
    'null',
    'file://',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:7080',
    'http://localhost:8080',

]


############# Session #######################
TokenConfig = {
    "alg": "HS256",
    "type": "JWT",
    "overtime": 86400   # 秒
}


# 数据库账号 Config
DBS = {
    "CURRENT_DB": "test",
    "deploy": {
        'db_type': 'mariadb',
        'db_ip': 'nas.superego',
        'db_name': 'twitterblocker',
        'db_user': 'vserver',
        'db_passwd': 'vserver00000000',
        'db_port': 3306,
        'timeout': 5,
        'charset': 'utf8'
    },
    "test": {
        'db_type': 'mariadb',
        'db_ip': 'nas.superego',
        'db_name': 'twitterblocker',
        'db_user': 'root',
        'db_passwd': 'nE7jA%5m..',
        'db_port': 3306,
        'timeout': 5,
        'charset': 'utf8'
    }
}