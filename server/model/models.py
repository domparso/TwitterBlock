#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

from model.native_model import *
from common.db import engine





# 从model生成表
if __name__ in "__main__":
    Base.metadata.create_all(engine)