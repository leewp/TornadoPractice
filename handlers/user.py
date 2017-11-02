#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import tornado.web


class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")
        self.render("user.html", users=(('', 'u_test', 'p_test', 'e_test'),))