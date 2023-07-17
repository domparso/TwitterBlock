#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com

sqlalchemy version 1.4 下 mssql与postgresql 报错 sqlacodegen github issue:131
"""

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker, Session
import sqlacodegen
import subprocess
from manage import ROOT_PATH, DBS
from model.tables import tableList
import os

dbInfo = DBS[DBS["CURRENT_DB"]]

target_path = os.path.join(ROOT_PATH, "../model/native_model.py")

if dbInfo["db_type"].upper() == "SQLSERVER":
    CONNECTSTR = r"mssql+pymssql://{}:{}@{}:{}/{}".format(dbInfo["db_user"],
                                                                  dbInfo["db_passwd"],
                                                                  dbInfo["db_ip"],
                                                                  dbInfo["db_port"],
                                                                  dbInfo["db_name"])
elif dbInfo["db_type"].upper() == "MARIADB" or dbInfo["db_type"].upper() == "MYSQL":
    CONNECTSTR = "mysql+pymysql://{}:{}@{}:{}/{} > {}".format(dbInfo["db_user"],
                                                                              dbInfo["db_passwd"].replace('@', '\@'),
                                                                              dbInfo["db_ip"],
                                                                              dbInfo["db_port"],
                                                                              dbInfo["db_name"],
                                                                              target_path)
elif dbInfo["db_type"].upper() == "SQLITE":
    CONNECTSTR = "sqlite+pysqlite://{}:{}@{}:{}/{} > {}".format(dbInfo["db_user"],
                                                                dbInfo["db_passwd"],
                                                                dbInfo["db_ip"],
                                                                dbInfo["db_port"],
                                                                dbInfo["db_name"],
                                                                target_path)

sqlacodegenArgs = {
    "url": '',  # 数据库连接符
    "schema": '',  # 数据库 schema load tables from an alternate schema
    "tables": [],  # 数据库 tables 默认: all
    "noviews": False,  # [True, False] 忽略视图
    "noindexes": False,  # [True, False] 忽略indexes
    "noconstraints": False,  # [True, False] 忽略constraints
    "nojoined": False,  # [True, False] 不要自动检测连接的表继承
    "noinflect": False,  # [True, False] 不要尝试将表名转换为单数形式
    "noclasses": False,  # [True, False] 不生成类，只生成表
    "nocomments": False,  # [True, False] 不呈现列注释
    "outfile": '',  # 文件输出 默认: stdout
}

def createmodels():

    cmd = "sqlacodegen "

    if sqlacodegenArgs["url"]:
        cmd = cmd + sqlacodegenArgs["url"] + ' '
    else:
        print("URL 数据库连接符不能为空")
        return

    if sqlacodegenArgs["schema"]:
        pass

    if sqlacodegenArgs["tables"]:
        cmd = cmd + '--tables '
        for table in sqlacodegenArgs["tables"]:
            cmd = cmd + table + ','
        cmd = cmd[:-1] + ' '

    if sqlacodegenArgs["noviews"]:
        cmd = cmd + "--noviews" + ' '

    if sqlacodegenArgs["noindexes"]:
        cmd = cmd + "--noindexes" + ' '

    if sqlacodegenArgs["noconstraints"]:
        cmd = cmd + "--noconstraints" + ' '

    if sqlacodegenArgs["nojoined"]:
        cmd = cmd + "--nojoined" + ' '

    if sqlacodegenArgs["noinflect"]:
        cmd = cmd + "--noinflect" + ' '

    if sqlacodegenArgs["noclasses"]:
        cmd = cmd + "--noclasses" + ' '

    if sqlacodegenArgs["nocomments"]:
        cmd = cmd + "--nocomments " + ' '

    # if sqlacodegenArgs["outfile"]:
    #     cmd = cmd + "--outfile " + sqlacodegenArgs["outfile"]

    print(cmd)
    p = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    out = str(p.stdout.read(), encoding='utf-8')
    print(out)

def modifyModelfile():
    # with
    pass

if __name__ == "__main__":
    sqlacodegenArgs["url"] = CONNECTSTR
    sqlacodegenArgs["tables"] = tableList
    sqlacodegenArgs["outfile"] = target_path
    createmodels()
    modifyModelfile()