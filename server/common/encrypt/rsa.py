#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Hash import MD5
from Cryptodome.Signature import pkcs1_15
import os

class RSAEncrypt():

    def __init__(self):
        self.public_key = None
        self.private_key = None

    def getPublicKey(self):
        return self.public_key

    def getPrivateKey(self):
        return self.private_key

    def setPublicKey(self, public_key):
        self.public_key = public_key
        if isinstance(self.public_key, str):
            self.public_key = bytes(self.public_key, encoding='utf-8')
        self.public_key = RSA.import_key(self.public_key)

    def setPrivateKey(self, private_key):
        self.private_key = private_key

    def loadPublicKey(self, file='public_key.pem'):
        # 导入公钥 public_key.pem
        self.public_key = RSA.import_key(open(file).read())

    def loadPrivateKey(self, file='private.pem'):
        # 导入公钥 private.pem
        self.private_key = RSA.import_key(open(file).read())

    def saveFile(self, path='./'):
        with open(os.path.join(path, 'private.pem'), 'wb') as f:
            f.write(self.private_key)
        with open(os.path.join(path, '../public_key.pem'), 'wb') as f:
            f.write(self.public_key)

    def generate_key(self):
        key = RSA.generate(1024)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def encrypt(self, data, encoding='utf-8'):
        if isinstance(data, str):
            data = bytes(data, encoding)
        cipher = PKCS1_OAEP.new(self.public_key)
        msg = cipher.encrypt(data)
        return msg

    def decrypt(self, data):
        cipher = PKCS1_OAEP.new(self.private_key)
        msg = cipher.decrypt(data)
        return msg

    def signaturer(self, data):
       digest = MD5.new(data)
       signature = pkcs1_15.new(self.private_key).sign(digest)
       return signature

    def checkSignaturer(self, data, signature):
        digest = MD5.new(data)
        pkcs1_15.new(self.public_key).verify(digest, signature)





if __name__ == "__main__":
    rsa = RSAEncrypt()
    rsa.generate_key()
    # print(rsa.getPublicKey())
    rsa.saveFile()