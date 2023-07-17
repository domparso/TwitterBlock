#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


import os
from manage import ROOT_PATH
from dao.user.customerdao import CustomerInfoDao

def generate(path):
    student = CustomerInfoDao()
    print(student.__dict__)
    for k in student.__dict__:
        print("def set_" + k + "(self," + k + "):")
        print("\tself." + k, "=" + k)
        print("def get_" + k + "(self):")
        print("\treturn self." + k)

    # manageFile = os.path.join(ROOT_PATH, path)
    #
    # with open(manageFile, 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     key = True
    #     with open(manageFile, 'w', encoding='utf-8') as f_w:
    #         for line in lines:
    #             if tmpStr in line and key:
    #                 key = False
    #             elif '"key":' in line and not key:
    #                 key = True
    #             else:
    #                 pass
    #             f_w.write(line)



if __name__ == "__main__":
    generate("dao/customer/customerdaoimpl.py", CustomerInfoDao)