#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

import base64
from Cryptodome import Random
from Cryptodome.Cipher import AES

class AESEncrypt():

    def __init__(self):
        self.key = Random.get_random_bytes(32)

        self.iv = Random.new().read(AES.block_size)

    def encrypt(self, data):
        """
        加密
        :param data:
        :return:
        """
        data = data.encode('utf8')
        data = (lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode('utf-8'))(data)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.iv.encode('utf8'))
        encryptedbytes = cipher.encrypt(data)
        encodestrs = base64.b64encode(encryptedbytes)
        enctext = encodestrs.decode('utf8')
        return enctext

    def decrypt(self, data):
        """
        解密
        :param data:
        :return:
        """
        data = data.encode('utf8')
        encodebytes = base64.decodebytes(data)
        cipher = AES.new(self.key.encode('utf8'), AES.MODE_CBC, self.iv.encode('utf8'))
        text_decrypted = cipher.decrypt(encodebytes)
        unpad = lambda s: s[0:-s[-1]]
        text_decrypted = unpad(text_decrypted)
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted
