#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The url structure of website
"""
import sys
from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.index import SleepHandler
from handlers.index import SeeHandler

reload(sys)
sys.setdefaultencoding("utf-8")

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler),
]