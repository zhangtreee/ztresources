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

def toBase64AndReverseAndSplit(file):
	with open(file,'rb') as fileObj:
		image_ata = fileObj.read()
		base64_data = base64.b64encode(image_ata)
		decoded_base64_data = base64_data.decode()
		decoded_base64_data = decoded_base64_data[::-1]
		for i in range(0,len(decoded_base64_data),1000 * 1000 * 24):
			file_name = file + '.' + str(i)
			fout = open(file_name, 'w')
			fout.write(decoded_base64_data[i:i+1000 * 1000 * 24])
			fout.close()
		# fout = open(txt,'w')
		# fout.write(base64_data.decode()[::-1])
		# fout.close()

def toFileFromSplit(files,outfile):
	entire_base64_data = ''
	for file in files:
		with open(file,'r') as fileObj:
			base64_data = fileObj.read()
			entire_base64_data += base64_data
		entire_base64_data = entire_base64_data[::-1]
		ori_image_data = base64.b64decode(entire_base64_data)
		fout = open(outfile, 'wb')
		fout.write(ori_image_data)
		fout.close()

def toFile(txt,file):
	with open(file,'r') as fileObj:
		base64_data = fileObj.read()
		base64_data = base64_data[::-1]
		ori_image_data = base64.b64decode(base64_data)
		fout = open(file,'wb')
		fout.write(ori_image_data)
		fout.close()

if __name__ == "__main__":
	file = "numpy-1.21.2+mkl-cp37-cp37m-win_amd64.whl"
	txt = file + ".txt"
	print("start toBase64 ...")
	# toBase64AndReverse(file,txt)
	toBase64AndReverseAndSplit(file)
	print("... finished toBase64")