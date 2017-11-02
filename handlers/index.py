#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import tornado.ioloop
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", user="tttt")

    def post(self):
        username = self.get_argument("username")
        print username
        password = self.get_argument("password")
        self.write(username)


class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time()+17)
        self.render("sleep.html", user="sleep")


class SeeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("see.html", user="see")

class Test_2:
    pass
