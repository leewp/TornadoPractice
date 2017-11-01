#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: www.baidu.com')