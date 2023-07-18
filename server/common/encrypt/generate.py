#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

import uuid
import time
import random
import json
import base64
from hashlib import sha256
from common.encrypt.token import JWT
from manage import WEBSERVERCONFIG, WS_CONFIG, TokenConfig

# 生成UUID
def generateUUID(username=None, uuidType=1):
    if uuidType == 1:
        return uuid.uuid1()
    elif uuidType == 3:
        return uuid.uuid3(uuid.NAMESPACE_DNS, username)
    elif uuidType == 4:
        return uuid.uuid4()
    elif uuidType == 5:
        return uuid.uuid5(uuid.NAMESPACE_DNS, username)
    else:
        return

# 生成Token
def generateJWT(uuid):
    """
    :param uuid:
    :return:
    """
    token = {}

    token["uri"] = WEBSERVERCONFIG["url"]
    token["iat"] = time.time()
    token["exp"] = time.time() + TokenConfig["overtime"]
    token["uuid"] = uuid
    token["iss"] = WS_CONFIG["serverUUID"]
    return JWT.encode(WS_CONFIG["serverKey"], token)

def generateVerifyCode(len):
    code_list = []
    for i in range(10):
        code_list.append(str(i))  #生成数字
    for i in range(65, 91):
        code_list.append(chr(i))   #生成大写字母
    # for i in range(97, 123):
    #     code_list.append(chr(i))   #生成小写字母
    r = random.sample(code_list, len)
    m = ''.join(r)
    return m

# 校验Token
def verifyToken(token):
    try:
        JWT.decode(token, WS_CONFIG["serverKey"])
        return True
    except Exception as e:
        return False