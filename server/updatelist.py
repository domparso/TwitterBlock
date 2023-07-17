#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


import requests
import os
import sys
import datetime


ROOT_PATH, CONFIGFILE = os.path.split(sys.argv[0])
cacheDir = './data'
blockDir = './blocklist'
gitUrl = 'https://raw.githubusercontent.com/domparso/TwitterBlock/master/blocklist/'



def get(filename):
    r = requests.get(gitUrl + filename, timeout=10)
    print(r.text)
    return r.text

def removeCRLF(p0):
    while '\n' in p0:
        p0.remove('\n')
    while '' in p0:
        p0.remove('')

def main():
    if not os.path.exists(cacheDir):
        print("blocklist 缓存目录不存在")
        return

    if not os.path.exists(os.path.join(ROOT_PATH, blockDir)):
        os.mkdir(os.path.join(ROOT_PATH, blockDir))

    pornBlockList = get('porn.txt').split('\n')
    removeCRLF(pornBlockList)
    otherBlockList = get('other.txt').split('\n')
    removeCRLF(otherBlockList)
    unblocklist = get('unblock.txt').split('\n')
    removeCRLF(unblocklist)
    logList = get('CHANGELOG.md').split('\n')
    removeCRLF(logList)


    if logList:
        lastLog = logList[-1]
        if lastLog == '' or lastLog == '\n':
            lastDate = datetime.datetime.strptime('2019-01-01', '%Y-%m-%d')
        else:
            lastDate = datetime.datetime.strptime(lastLog, '%Y-%m-%d')
    else:
        lastDate = datetime.datetime.strptime('2019-01-01', '%Y-%m-%d')


    userIdPornList = []
    for item in pornBlockList:
        userIdPornList.append(item.split(',')[0])

    userIdOtherList = []
    for item in otherBlockList:
        userIdOtherList.append(item.split(',')[0])

    userIdunBlockList = []
    for item in unblocklist:
        userIdunBlockList.append(item.split(',')[0])


    for dir in os.listdir(cacheDir):
        currDate = datetime.datetime.strptime(dir, '%Y-%m-%d')
        if currDate <= lastDate:
            continue

        child_dir = os.path.join(cacheDir, dir)

        if os.path.exists(os.path.join(child_dir, "porn")):
            with open(os.path.join(child_dir, "porn"), 'r', encoding='utf-8') as f:
                tmpList = f.read().split('\n')
            for item in tmpList:
                if item.split(',')[0] and item.split(',')[0] not in userIdPornList and item.split(',')[0] not in userIdunBlockList:
                    pornBlockList.append(item)

        if os.path.exists(os.path.join(child_dir, "other")):
            with open(os.path.join(child_dir, "other"), 'r', encoding='utf-8') as f:
                tmpList = f.read().split('\n')
            for item in tmpList:
                if item.split(',')[0] and item.split(',')[0] not in userIdOtherList and item.split(',')[0] not in userIdunBlockList:
                    otherBlockList.append(item)

        if os.path.exists(os.path.join(child_dir, "unblock")):
            with open(os.path.join(child_dir, "unblock"), 'r', encoding='utf-8') as f:
                tmpList = f.read().split('\n')
            for item in tmpList:
                if item.split(',')[0] and item.split(',')[0] not in userIdOtherList and item.split(',')[0] not in userIdunBlockList:
                    unblocklist.append(item)

        logList.append(dir)
    print(pornBlockList)
    print(logList)

    with open(os.path.join(ROOT_PATH, blockDir, 'porn.txt'), 'w', encoding='utf-8') as f:
        f.write(('\n').join(pornBlockList))
    with open(os.path.join(ROOT_PATH, blockDir, 'other.txt'), 'w', encoding='utf-8') as f:
        f.write(('\n').join(otherBlockList))
    with open(os.path.join(ROOT_PATH, blockDir, 'unblock.txt'), 'w', encoding='utf-8') as f:
        f.write(('\n').join(unblocklist))
    with open(os.path.join(ROOT_PATH, blockDir, 'CHANGELOG.md'), 'w', encoding='utf-8') as f:
        f.write(('\n').join(logList))


    print("更新完成")





if __name__ == '__main__':
    main()