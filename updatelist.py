#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""

import os



cachDir = './blocklist/cache'
blockDir = './blocklist'





def main():
    if not os.path.exists(cachDir):
        print("blocklist 缓存目录不存在")
        return

    with open(os.path.join(blockDir, 'porn.txt'), 'r', encoding='utf-8') as f:
        pornBlockList = f.readlines()

    userIdPornList = []
    for item in pornBlockList:
        userIdPornList.append(item.split(',')[0])

    with open(os.path.join(blockDir, 'other.txt'), 'r', encoding='utf-8') as f:
        otherBlockList = f.readlines()

    userIdOtherList = []
    for item in otherBlockList:
        userIdOtherList.append(item.split(',')[0])

    with open(os.path.join(blockDir, 'unblock.txt'), 'r', encoding='utf-8') as f:
        unblocklist = f.readlines()

    userIdunBlockList = []
    for item in unblocklist:
        userIdunBlockList.append(item.split(',')[0])

    for dir in os.listdir(cachDir):
        child_dir = os.path.join(cachDir, dir)
        for file in os.listdir(child_dir):
            if file == "porn":
                tmpPornList = []
                with open(os.path.join(child_dir, file), 'r', encoding='utf-8') as f:
                    tmpList = f.readlines()
                for item in tmpList:
                    if item.split(',')[0] not in userIdPornList and item.split(',')[0] not in userIdunBlockList:
                        tmpPornList.append(item)
                with open(os.path.join(blockDir, 'porn.txt'), 'w+', encoding='utf-8') as f:
                    f.writelines(tmpPornList)
            elif file == "other":
                tmpOtherList = []
                with open(os.path.join(child_dir, file), 'r', encoding='utf-8') as f:
                    tmpList = f.readlines()
                for item in tmpList:
                    if item.split(',')[0] not in userIdOtherList and item.split(',')[0] not in userIdunBlockList:
                        tmpOtherList.append(item)
                with open(os.path.join(blockDir, 'other.txt'), 'w+', encoding='utf-8') as f:
                    f.writelines(tmpOtherList)

            with open(os.path.join(blockDir, 'CHANGELOG.md'), 'w+', encoding='utf-8') as f:
                f.writelines(file)


    print("更新完成")





if __name__ == '__main__':
    main()