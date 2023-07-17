#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


from tornado import gen
from manage import SAVE_PATH
import datetime
import os
import logging


@gen.coroutine
def writeFile(p0):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    try:
        if not os.path.exists(SAVE_PATH):
            os.mkdir(SAVE_PATH, 755)

        if not os.path.exists(os.path.join(SAVE_PATH, now)):
            os.mkdir(os.path.join(SAVE_PATH, now), 755)
    except Exception as e:
        print(e)
        return
    # logging.debug("写入数据...", SAVE_PATH + now)
    with open(os.path.join(SAVE_PATH, now, p0[0]), 'a', encoding='utf-8') as f:
        f.write(','.join(p0[1:]) + '\n')
        f.flush()