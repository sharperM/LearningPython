# -*- coding: UTF-8 -*-
import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

form PIL import Image
im = Image.open("test.jpg")
print im.format, im.size, im.mode
im.thumbnail((100,100))

im.save('thumb.jpg','JPEG')
