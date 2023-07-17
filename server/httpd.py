#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: domparso
email: domparso@hotmail.com
"""


import tornado.ioloop
import tornado.web
from routes import urlpatterns

import nest_asyncio
nest_asyncio.apply()



class Application(tornado.web.Application):

    def __init__(self, ping_interval, ping_timeout):
        super(Application, self).__init__()
        self.websocket_ping_interval = ping_interval,       # 间隔5秒发送一次ping帧，第一次发送为触发的5s后
        self.websocket_ping_timeout = ping_timeout


def make_app():
    return tornado.web.Application(urlpatterns)



if __name__ == "__main__":
    import server
    # server init
    server.init()
    # server init and deamon
    server.deamon()
    app = make_app()
    app.listen(7080)

    tornado.ioloop.IOLoop.current().start()