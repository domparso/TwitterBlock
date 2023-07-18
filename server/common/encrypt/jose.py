#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

import time
import json
import copy
from jose import jwe, jwt, jws


class JWE(object):

    @staticmethod
    def encode(self_payload, key=None, algorithm='dir', encryption='A128GCM'):
        """
        :param self_payload: 'Hello, World!'
        :param key: 'asecret128bitkey'
        :param algorithm: DIR/RSA1_5/RSA_OAEP/RSA_OAEP_256/A128KW/A192KW m/A256KW
        :param encryption: A128CBC_HS256/A192CBC_HS384/A256CBC_HS512/A128GCM/A192GCM/A256GCM
        :return:
        """
        self_payload_copy = copy.deepcopy(self_payload)
        if not isinstance(self_payload_copy, str):
            self_payload_copy = json.dumps(self_payload_copy, separators=(',', ':'), sort_keys=True)

        return jwe.encrypt(self_payload_copy, key, algorithm=algorithm, encryption=encryption)

    @staticmethod
    def decode(token, key):
        """
        传入jwt的值(令牌) 和只有调用者知道的key
        :param token:
        :param key: 'asecret128bitkey'
        :return:
        """

        payload = jwe.decrypt(token, key)
        # now = time.time()  # 当前时间
        # if int(now) > int(payload["exp"]):  # 登录时间过期
        #     raise
        return payload  # 返回自定义内容


class JWT(object):

    @staticmethod
    def encode(self_payload, key=None):
        """
        :param self_payload: {'key': 'value'} {}
        :param key: 'secret'
        :return: token
        """

        return jwt.encode(self_payload, key, algorithm='HS256')

    @staticmethod
    def decode(token, key):
        """
        传入jwt的值(令牌) 和只有调用者知道的key
        :param token:
        :param key: 'secret'
        :return:
        """
        payload = jwt.decode(token, key, algorithms=['HS256'])
        now = time.time()  # 当前时间
        if int(now) > int(payload["exp"]):  # 登录时间过期
            raise
        return payload  # 返回自定义内容


class JWS(object):

    @staticmethod
    def encode(self_payload, key=None):
        """
        :param self_payload: {'key': 'value'} {}
        :param key: 'secret'
        :param algorithms: HS256/HS384/HS512/RS256/RS384/RS512/ES256/ES384/ES512
        :return: signed
        """

        return jws.sign(self_payload, key, algorithm='HS256')

    @staticmethod
    def decode(signed, key):
        """
        传入jwt的值(令牌) 和只有调用者知道的key
        :param token:
        :param key: 'secret'
        :return: payload
        """

        payload = jws.decode(signed, key, algorithms=['HS256'])
        return payload  # 返回自定义内容
