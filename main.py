#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner
email: nbxlc@hotmail.com
"""

from simplejson import dumps, loads, load, dump
import threading
from http.server import HTTPServer
from socketserver import ThreadingMixIn
import subprocess
from http.server import BaseHTTPRequestHandler
from os import path
import multiprocessing
import sys, os
import time, datetime
from queue import Queue
import platform

os_platform = platform.system()

# from urllib.parse import urlparse

PORT = 8090
WAITTIME = 600
SAVE_PATH = './'

DATA_DICT = Queue()

curdir = path.dirname(path.realpath(__file__))
sep = '/'

# MIME-TYPE
mimedic = [('.html', 'text/html'),
            ('.htm', 'text/html'),
            ('.js', 'application/javascript'),
            ('.css', 'text/css'),
            ('.json', 'application/json'),
            ('.png', 'image/png'),
            ('.jpg', 'image/jpeg'),
            ('.gif', 'image/gif'),
            ('.txt', 'text/plain'),
            ('.avi', 'video/x-msvideo'),
            ]


class HTTPServerHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        print("GET 接收数据中")
        print("host", self.headers["host"])
        print("header", self.headers)
        print("path", self.path)
        self.send_error(404, "File not found.")

    def do_POST(self):
        print("POST 接收数据中")
        if self.path != "/api/v1/twitterblocker/set":
            self.send_error(404, "File not found.")
            return

        content_Type = self.headers['Content-Type']
        if content_Type != "application/json" and "application/json;" not in content_Type.lower():
            self.send_error(415, "Format parsing error.")
            return

        response = '0'
        try:
            content_length = int(self.headers['content-length'])
            post_data = loads(self.rfile.read(content_length).decode('utf-8'))
            print("post_data", post_data)
            if self.path == "/api/v1/twitterblocker/set":
                response = '1'
                global DATA_DICT
                DATA_DICT.put(post_data)
                print("DATA_DICT", DATA_DICT.qsize())

            else:
                response = '0'
        except Exception as e:
            print(e)

        self._set_headers()
        self.wfile.write(bytes(response, encoding='utf-8'))


class WFThread(threading.Thread):

    def __init__(self, queque):
        super(WFThread, self).__init__()
        self.stopBool = False
        self.queque = queque

    def setParm(self, data):
        self.queque.put(data)

    def run(self):
        self.stopBool = False
        print("wfTh线程开启")
        while not self.stopBool:
            print("WF DATA_DICT", self.queque.qsize())
            if not DATA_DICT.empty():
                print("接收数据...")
                data = DATA_DICT.get()
                self.writeFile(data)
            else:
                time.sleep(60)

    def stop(self):
        self.stopBool = True

    def writeFile(self, p0):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            if not os.path.exists(SAVE_PATH):
                os.mkdir(SAVE_PATH, 755)

            if not os.path.exists(os.path.join(SAVE_PATH, now)):
                os.mkdir(os.path.join(SAVE_PATH, now), 755)
        except Exception as e:
            print(e)
            return
        print("写入数据...", SAVE_PATH+now)
        with open(os.path.join(SAVE_PATH+now, p0[0]), 'a', encoding='utf-8') as f:
            f.write(','.join(p0[1:]) + '\n')
            f.flush()


class ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass


class HTTPProcess(multiprocessing.Process):

    def __init__(self, parent=None):
        super(HTTPProcess, self).__init__(parent)

    def run(self):

        p = subprocess.Popen("kill -9 $(lsof -i:{} | awk '{{print $2}}' | tail -n 2)".format(60),
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        out = p.stdout.readlines()

        for res in out:
            print(str(res, encoding='utf-8'))

        try:
            wfTh = WFThread(DATA_DICT)
            wfTh.start()

            # Server settings
            server_address = ('', PORT)
            self.httpd = ThreadingHttpServer(server_address, HTTPServerHandler)
            self.httpd.request_queue_size = 20
            print('running server...')
            self.httpd.serve_forever()
            return self.httpd
        except Exception as e:
            self.httpd.socket.close()
        raise Exception

    def stop(self):
        try:
            self.terminate()
        except Exception as e:
            print(e)

    def getState(self):
        if self.is_alive():
            return True
        return False




if __name__ == "__main__":
    hp = HTTPProcess()
    # wfTh = WFThread(DATA_DICT)

    while True:
        if not hp.is_alive():
            hp.start()
        # if not wfTh.is_alive():
        #     wfTh.start()

        while True:
            if 'windows' not in os_platform.lower():
                p = subprocess.Popen("ps -ef | grep " + sys.argv[0],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True)
                out = p.stdout.readlines()
                if len(out) <= 1:
                    print("HTTP程序崩溃，正在重启...")
                    time.sleep(10)
                    break
                time.sleep(WAITTIME)
            else:
                time.sleep(WAITTIME)
