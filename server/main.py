#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""

import sys
import argparse
import getopt
import logging.handlers
import os
from shutil import copyfile
from manage import os_platform, ROOT_PATH, CONFIGLIST
# from pycrunch_trace.client.api import trace


def log(LOGLEVEL):
    levels = [logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG]
    logPath = os.path.join(ROOT_PATH, 'logs')
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    LOG_FILE = os.path.join(logPath, 'tornado.log')
    logger = logging.getLogger("myapp")
    hdlr = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024*10240, backupCount=400, encoding='utf-8')     # 按大小进行分割
    # hdlr = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='D', interval=1, backupCount=40)  # 按时间进行分割
    logging.basicConfig(level=levels[LOGLEVEL],
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=LOG_FILE,
                        filemode='a+')
    logger.addHandler(hdlr)
    logger.setLevel(LOGLEVEL)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def create_file(filename):
    """
    创建日志文件夹和日志文件
    :param filename:
    :return:
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()

# @trace()
def main(*argv,  **kwargs):
    if not argv:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ha", ["help", "action="])
            # print(opts, args)

            # parser = argparse.ArgumentParser()
            # parser.add_argument('action')
            # # args = parser.parse_args()
            # args, unknown = parser.parse_known_args()
            # print(args, unknown)

            # log enable
            log(int(CONFIGLIST["server"]["loglevel"]))

            # listener
            import httpd
            app = httpd.make_app()

            # sockets = httpd.tornado.netutil.bind_sockets(CONFIGLIST["server"]["port"])
            # httpd.tornado.process.fork_processes(0)
            # tornadoServer = httpd.tornado.httpserver.HTTPServer(app)
            # tornadoServer.add_sockets(sockets)

            app.listen(CONFIGLIST["server"]["port"])
            # 多进程模式 windows下不支持
            # if 'windows' not in os_platform.lower():
            #     tornadoServer = httpd.tornado.httpserver.HTTPServer(app)
            #     tornadoServer.start(0)                             # forks one process per cpu

            httpd.tornado.ioloop.IOLoop.current().start()

        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2


if __name__ == "__main__":
    # sys.exit(main())
    sys.exit(main(env='dev'))
