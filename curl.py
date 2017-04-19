#!/usr/bin/env python
# coding=utf-8

import pycurl
import StringIO

response = StringIO.StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://api.ipify.org')
c.setopt(c.WRITEFUNCTION, response.write)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
c.setopt(c.POSTFIELDS, '@request.json')
c.perform()
c.close()
print response.getvalue()
response.close()
