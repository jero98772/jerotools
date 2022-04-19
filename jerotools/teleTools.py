#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
from urllib import request
from socket import gethostname ,gethostbyname
def webIsOniline(web):
	"""webIsOniline(<web for check>) , Return true or False"""
	if web == "":
		return False
	else:	
		status = request.urlopen(web).getcode()
		if status == 200:
			return True
		else: 
			return False
def getData():
	"""get ip and hostname when you acces to this web"""
	hostname = gethostname()
	ip = gethostbyname()
	return ip, hostname
def getImg(url,imgname):
	"""
	get image form url 
	"""
	import requests
	imgrequ = requests.get(url).content
	with open(imgname, "wb") as file:
		file.write(imgrequ)