# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 15:36
# @Author  : zhangweijun
# @File    : tobase64.py

import base64

def toBase64AndReverse(file,txt):
	with open(file,'rb') as fileObj:
		image_ata = fileObj.read()
		base64_data = base64.b64encode(image_ata)
		fout = open(txt,'w')
		fout.write(base64_data.decode()[::-1])
		fout.close()

def toFile(txt,file):
	with open(file,'r') as fileObj:
		base64_data = fileObj.read()
		base64_data = base64_data[::-1]
		ori_image_data = base64.b64decode(base64_data)
		fout = open(txt,'wb')
		fout.write(ori_image_data)
		fout.close()

if __name__ == "__main__":
	file = "python_Levenshtein-0.12.2-cp37-cp37m-win_amd64.whl"
	txt = file + ".txt"
	print("start toBase64 ...")
	toBase64AndReverse(file,txt)
	print("... finished toBase64")