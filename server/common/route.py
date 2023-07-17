#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


def path(url_re, patterns):
    urlpatterns = []
    for pattern in patterns:
        if pattern[0]:
            if url_re[-1] == '/':
                urlpatterns.append((url_re + pattern[0], pattern[1]))
            else:
                urlpatterns.append((url_re + '/' + pattern[0], pattern[1]))
        else:
            urlpatterns.append((url_re, pattern[1]))
    return urlpatterns

