#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


from common.handler import MainHandler, setRspStatus
from tornado.websocket import Optional, Awaitable, Union
import logging
import json
from common.jsontools import NewEncoder


class IndexHandler(MainHandler):

    callbackDict = {}

    def post(self, *args: str, **kwargs: str):
        super(IndexHandler, self).post(args, kwargs)

        response = {"response": {}}

        try:
            requset_data = super().on_message(message)
            if not requset_data:
                return
            logging.debug("requset_data: {}".format(requset_data))
            if not requset_data or not requset_data.__contains__("action") or not requset_data["action"]:
                return

            if not requset_data.__contains__("request"):
                setRspStatus(response, "2101")

            response["action"] = requset_data["action"]
            logging.debug(self.callbackDict)
            if not self.callbackDict.__contains__(requset_data["action"]) \
                    or self.callbackDict[requset_data["action"]]:
                self.callbackDict[requset_data["action"]](self, requset_data, response)
            else:
                setRspStatus(response, "2200")
                logging.error("未知的action: {}".format(response["action"]))

        except Exception as e:
            logging.debug(e)
            setRspStatus(response, "2101")

        self.write(json.dumps(response, cls=NewEncoder))


    # def select_subprotocol(self, subprotocols: List[str]) -> Optional[str]:
    #     print("subprotocols", subprotocols)
