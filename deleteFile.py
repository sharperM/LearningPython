# -*- coding: UTF-8 -*-     
import os
#os.remove("E:\\KuGou\\temp\\d6704384ddf91435905aa1da81672d04.mp3")
#os.remove("E:\\KuGou\\temp\\4bfa62213e6badab50fce7fc0c8d9b68.mp3")
#os.remove("E:\\KuGou\\temp\\c0751c7ee4c0f32f2a54753383800031.mp3")

fw = open(os.path.join("E:\\KuGou","1234..txt"), 'rb')
(filepath,filename)=os.path.split(fw.name)
print ((filepath,filename))
print os.path.splitext(filename)
