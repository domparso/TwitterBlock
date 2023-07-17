#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler, Optional, Awaitable, Union, Any, Dict
from tornado.escape import json_decode
# from tornado import httputil
import json.decoder
import logging
import re
# import urllib
import manage



class MainHandler(RequestHandler):

    # 跨域访问设置
    def allowMyOrigin(self):
        if 'Origin' in self.request.headers:
            # print(self.request.headers)
            Origin = self.request.headers['Origin']
            # 域名
            re_ret = re.match(r".{1,}\.({" + manage.CONFIGLIST['origin'] + "})", Origin)
            # 内网和本地
            re_ret2 = re.match(r"^(192.168.1.*|127.0.0.1.*|192.168.2.*)", Origin)
            if re_ret or re_ret2 or Origin in manage.CORS_LIST:
                self.set_header("Access-Control-Allow-Origin", Origin)              # 这个地方可以写域名也可以是*
                self.set_header("Access-Control-Allow-Headers", "*")
                # self.set_header('Access-Control-Allow-Headers', 'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
                self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def set_default_headers(self) -> None:
        self.allowMyOrigin()

    # def get(self, *args: str, **kwargs: str):
    #     self.jsonFormat_interceptor(args, kwargs)
    #
    # def options(self):
    #     pass

    def post(self, *args: str, **kwargs: str):
        self.jsonFormat_interceptor(args, kwargs)

    def jsonFormat_interceptor(self, *args: str, **kwargs: str):
        headers = self.request.headers
        # logging.debug("headers {}".format(headers))
        if headers["Content-Type"] != "application/json":
            return self.write_error(417)
        try:
            self.requset_data = json_decode(self.request.body)
        except json.decoder.JSONDecodeError:
            logging.error("{} {} {} json格式解码错误".format(self.request.path, headers, self.request.body))
            return self.write_error(400)

        logging.debug("requset_data {}".format(self.requset_data))


def setRspStatus(response, code=None):
    if not code:
        response["status"] = 'ok'
    else:
        response["status"] = "error"
        if type(code) == int:
            response["err-code"] = str(code)
        else:
            response["err-code"] = code

def HandlerInterceptor(func):

    def pre_interceptor():
        pass

    def suf_interceptor():
        pass

    pre_interceptor()
    func()
    suf_interceptor()