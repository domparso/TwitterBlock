#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


from manage import WEBSERVERCONFIG
from .twiter.blocker import BlockHandler

# action loader 各个模块都需要初始化加载



urlpatterns = [
    (r'^' + WEBSERVERCONFIG["uri"] + '/twitterblocker/set', BlockHandler),
]
