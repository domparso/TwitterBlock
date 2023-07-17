#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing factory.
author: Reiner
email: nbxlc@hotmail.com
"""

import importlib
import manage

def getShape(moduleName, className):
    if manage.DBS.get(manage.DBS["CURRENT_DB"]):

        # from action import secondimpl
        # clsdao = getattr(getattr(secondimpl, moduleName), className)

        # module = importlib.import_module("action.secondimpl." + moduleName)
        module = importlib.import_module("dao.impl." + moduleName)
    else:
        raise Exception("数据配置错误")

    clsdao = getattr(module, className)
    return clsdao
