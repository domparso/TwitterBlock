#!/bin/bash
# -*- coding: utf-8 -*-
#
# Module implementing MaintenanceWindow.
# author: domparso
# email: domparso@hotmail.com
#


PYTHON=python3

# 生成项目的requirements.txt，只扫描依赖库
# pipqreqs.py 修改 line:121 忽略 "/model"目录
# print("file_name", file_name)
# if "/model" in file_name:
#     continue
#
# 安装项目的依赖库
# pip install -r requriements.txt



set -e

cd $(dirname $0)

if [[ $1 = "install" ]]; then
  file=requirements.txt
  if [ $2 ]; then
    file=$2
  fi

  $PYTHON -m pip install -r $file
else
  # 创建 requirements.txt 使用自编译wheel安装 # --ignore ./model 忽略model目录
  pipreqs ./ --encoding=utf8 --ignore ./model
fi


