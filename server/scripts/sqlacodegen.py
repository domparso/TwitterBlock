#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""



import os
from manage import DBS, ROOT_PATH
# from common.db import engine

# sqlacodegen mysql://user:password@domain:port/databasename > models.py

MODELPATH = "../model/native_model.py"
db = DBS[DBS["CURRENT_DB"]]
db_type = ''
if db["db_type"] == "mariadb":
    db_type = "mysql"
else:
    db_type = db["db_type"]

cmd = "sqlacodegen {}://{}:{}@{}:{}/{}?charset={} > {}".format(
    db_type,
    db["db_user"],
    db["db_passwd"],
    db["db_ip"],
    db["db_port"],
    db["db_name"],
    db["charset"],
    MODELPATH
)

os.system(cmd)
