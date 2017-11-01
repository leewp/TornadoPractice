#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(host='localhost', user='tornado', passwd='password', db='tornadotest', port=3306)
cur = conn.cursor()