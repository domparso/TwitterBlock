#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""

from common.handler import MainHandler, setRspStatus
from tornado.websocket import Optional, Awaitable, Union

from common.jsontools import NewEncoder


from service.factory import getShape
from service.index import IndexHandler, setRspStatus
from service.twiter.asyn import writeFile
import json
import logging


def auth(handler, requset_data, response):
    if not requset_data.__contains__("request"):
        setRspStatus(response, "2101")
        return

    request = requset_data["request"]
    try:
        nodeDao = getShape("site.nodedaoimpl", "NodeDaoImpl")()
    except Exception as e:
        logging.error(e)

    result = nodeDao.getNodeById(request["siteId"])
    # 对客户侧， 数据需裁剪
    if result == 1:
        response["response"]["state"] = nodeDao.state
        setRspStatus(response)
    elif request == 0:
        response["response"]["state"] = '-1'
        setRspStatus(response)
    else:
        setRspStatus(response, '2421')
        logging.error('查询异常')

IndexHandler.callbackDict["auth"] = auth


class BlockHandler(MainHandler):

    def post(self, *args: str, **kwargs: str):
        super(BlockHandler, self).post(args, kwargs)

        response = {"response": {}}

        try:
            if not self.requset_data:
                return
            logging.debug("requset_data: {}".format(self.requset_data))

            writeFile(self.requset_data)
            return self.write("1")

        except Exception as e:
            logging.debug(e)
            setRspStatus(response, "2101")

        self.write(json.dumps(response, cls=NewEncoder))

