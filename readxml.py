# -*- coding: UTF-8 -*-
import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
	import xml.etree.cElementTree as ET
except ImportError:
	import xml.etree.ElementTree as ET

try:
	tree = ET.parse("sealy_update.xml")
	root = tree.getroot()
except Exception, e:
	print "Error:cannot parse file:sealy_update.xml"
	sys.exit(1)


import hashlib
def md5_for_file(f, block_size=2**20): 
    md5 = hashlib.md5() 
    while True: 
        data = f.read(block_size) 
        if not data: 
            break 
        md5.update(data) 
    return md5.hexdigest() 

from datetime import time,datetime
print 
# print root.tag,"---",root.attrib
# for child in root:
# 	print child.tag,"---",child.attrib
# print "*"*10
# strversion = root.get('version')
# strKeyMD5 = root.get('KeyMD5')
# print strversion,strKeyMD5

f = open('GamePlaza.exe', 'rb')
strMd5 = md5_for_file(f)

import string
print string.upper(strMd5)
root.set("KeyMD5",string.upper(strMd5))
root.set("version",datetime.strftime(datetime.now(),'%Y%m%d%H%M%S'))
def write_xml(tree, out_path):  
    '''''将xml文件写出 
       tree: xml树 
       out_path: 写出路径'''  
    tree.write(out_path, encoding="utf-8",xml_declaration=True)  

write_xml(tree,"1.xml")