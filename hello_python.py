# -*- coding: UTF-8 -*-     
import os
import os.path
#print os.name
#print os.getenv('PATH')
import sys
type = sys.getfilesystemencoding()

#try:
#    f = open('F:\\msp_project\\msp.txt', 'r')
#    print f.read()
#finally:
#    if f:
#        f.close()
#
#for x in xrange(1,11):
#	os.mkdir('F:\\msp_project\\test______dir'+str(x))
#
#for x in xrange(1,11):
#	os.rmdir('F:\\msp_project\\test______dir'+str(x))



def listSameSizeFilePath(root):
	allfileSize_Path = {}
	for parent,dirnames,filenames in os.walk(root):    
		for dirname in  dirnames:                     
			pass
		for filename in filenames:                    
			nSize = os.path.getsize(os.path.join(parent,filename))
			if allfileSize_Path.get(nSize) == None:
				allfileSize_Path[nSize]=[]
			allfileSize_Path[nSize].append(os.path.join(parent,filename))	
			pass
	return allfileSize_Path
#查找文件名相似的文件
def listSameNameFilePath(root):
	allFileName_path = {}
	allSimilarityName = []
	#找所有相同名字的文件名
	for parent,dirnames,filenames in os.walk(root):    
		for dirname in  dirnames:                     
			pass
		for filename in filenames:
			(name,type_)=os.path.splitext(filename)                    
			if allFileName_path.get(name) == None:
				allFileName_path[name]=[]
			allFileName_path[name].append(os.path.join(parent,filename))
	#找出一个文件名是 另一个文件名字的 子集，且是从第一个字符就匹配
	for fname1,path1 in allFileName_path.iteritems():
		similarityName = []
		similarityName.append(fname1)
		for fname2,path2 in allFileName_path.iteritems():
			if fname1.find(fname2) == 0:
				if fname1!=fname2:
					similarityName.append(fname2)
				
		if len(similarityName)>1:
			allSimilarityName.append(similarityName)
	return allFileName_path,allSimilarityName
import hashlib
def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()
#E:\\KuGou
#F:\\下载\\
rootdir = 'E:\\KuGou'
samesize = listSameSizeFilePath(rootdir)


i = 0
j = 0
nWriteTime = 0
md5_filePath = {}
for paths in samesize.itervalues():
	if len(paths)>1:
		for filePath in paths:
			f = None
			fw = None
			try:
			    f = open(filePath, 'rb')
			    strMd5 = md5_for_file(f)
			    if md5_filePath.get(strMd5) == None:
			    	md5_filePath[strMd5] = []
			    md5_filePath[strMd5].append(filePath)
			    
			finally:
			    if f:
			        f.close()
		i = i+1
for strMMd5,sameFilePath in md5_filePath.iteritems():
	if len(sameFilePath)>1:
		print "MD5:"+strMMd5
		print sameFilePath
		#for filePath in sameFilePath:
		#	print filePath.decode("utf-8")
		#	print unicode(filePath,"utf-8")
		#	pass
		#print "------------"
		j = j+1
try:
	fw = open(os.path.join(rootdir,"log.txt"), 'w')
	for strMMd5,sameFilePath in samesize.iteritems():
		#fw.write(strMd5)
		fw.write('\n')
		ii = 0
		for fileName in sameFilePath:
			if len(sameFilePath)>1:
				if ii == 0:	
					fw.write("os.remove(\""+fileName+"\")")
					fw.write('\n')

			ii = ii + 1
finally:
	if fw:
		fw.close()


print "same size count:"+str(i)
print "same md5 count:"+str(j)
print "write Time count:"+str(nWriteTime)


(sameNameFiles, similarityNameFiles) = listSameNameFilePath(rootdir)

try:
	fw = open(os.path.join(rootdir,"log1.txt"), 'w')
	print "--------------------"
	fw.write("------相同的------\r\n")
	for k,v in sameNameFiles.iteritems():
		if len(v)>1:
			fw.write(k)
			fw.write('\r\n')
			for ppath in v:
				fw.write(ppath)
				fw.write('\r\n')
	print "--------------------"
	fw.write("------相似的------\r\n")
	for names in similarityNameFiles:
		for name in names:
			if len(names)>1:
				fw.write(name)
				fw.write('\r\n')
finally:
	if fw:
		fw.close()

