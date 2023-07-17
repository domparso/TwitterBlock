#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

from copy import deepcopy

class BaseDao(object):

    def __init__(self):
        self.nested = False

    def generateFunc1(self):
        """
        针对变量值为普通变量
        :return:
        """

        for key in deepcopy(self.__dict__):
            getFuncStr = "def get_{}(self):\n\treturn self.{}".format(key.split('__')[-1], key)
            setattr(self, "get_{}".format(format(key.split('__')[-1])), compile(getFuncStr, "<string>", "exec"))

            setFuncStr = "def set_{}(self, p0):\n\tself.{} = p0".format(key.split('__')[-1], key)
            setattr(self, "set_{}".format(format(key.split('__')[-1])), compile(setFuncStr, "<string>", "exec"))

            setattr(self,
                    key.split('__')[-1],
                    property(
                        getattr(self, "get_{}".format(key.split('__')[-1])),
                        getattr(self, "get_{}".format(key.split('__')[-1])))
                    )
            setattr(self, key.split('__')[-1], None)

    def generateFunc2(self):
        """
        针对变量值为对象或者特殊变量
        :return:
        """

        for key in deepcopy(self.__dict__):
            getFuncStr = "@property\ndef {}(self):\n\treturn self.{}".format(key.split('__')[-1], key)
            setattr(self, key.split('__')[-1], compile(getFuncStr, "<string>", "exec"))

            setFuncStr = "@{}.setter\ndef {}(self, p0):\n\tself.{} = p0".format(key.split('__')[-1], key.split('__')[-1], key)
            setattr(self, "{}".format(format(key.split('__')[-1])), compile(setFuncStr, "<string>", "exec"))

            setattr(self, key.split('__')[-1], None)
