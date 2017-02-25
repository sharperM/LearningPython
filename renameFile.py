# -*- coding: utf-8 -*-
import os
import sys
# import chardet
path = 'C:\\Users\\admin\\Desktop\\日志'.decode("utf-8").encode('gbk')
reload(sys)
sys.setdefaultencoding('UTF-8')
filename = {"11212":"11111","新建文本文档 - 副本".decode("utf-8").encode("gbk"):1}
# filename = {"112121":1,"新建文本文档 - 副本":1}
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.')<0:
#        print file.split('.')[-1] 
            newname=file+'rsfdjndk.jpg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
       	# print file.split('.')[0]
       	dd = file.split('.')[0]
       	if filename.has_key(dd) :
       		newname=filename[dd]
       		os.rename(os.path.join(path,file),os.path.join(path,newname))
       		# print (dd.decode('gbk').encode("utf-8"))
       		# print (dd.decode('gbk').encode("utf-8"))
       		# print (dd)
print "1212"

for x in filename:
	# print unicode("拉萨的肌肤","")

	print x.decode('gbk').encode("utf-8")

print(hex(hash("123")))

with open('C:\\Users\\admin\\Desktop\\日志\\测试 “登录服务器” .txt'.decode("utf-8").encode('gbk')) as fp:
    for line in iter(fp.readline, ''):
        print(line.decode("gbk").encode('utf-8'))
