#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""

from common.db import engine
from model.native_model import Base

Base.metadata.create_all(engine)