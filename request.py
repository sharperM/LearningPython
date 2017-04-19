#!/usr/bin/env python
# coding=utf-8


from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address is: {}'.format(ip))
