#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
def img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
	"""
	img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]) ,return a  matrix img as str
	"""
	import cv2
	from numpy import asarray 
	dataFile = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
	imgresized  = cv2.resize(dataFile , (size, size))
	imgstr = ""
	#imgstr = asarray(imgresized , dtype= str)
	for count in range(len(imgresized)):
		for cont in range(len(imgresized[count]))  :
				if imgresized[count,cont]//intensity == replaceItem:
					#imgstr[count,cont]= items[0]
					imgstr += items[0]
				else:
					#imgstr[count,cont] = items[1]
					imgstr += items[1]
		imgstr += "\n"
	outfig = [imgresized,imgstr]
	print(imgstr)
	return outfig 
def webTranslate(txt,writeIn,translateTo):
	"""
	webTranslate(txt,writeIn,translateTo )
	  - txt			  -text to trasnlate
	  - writeIn		  -in which language is it written
	  - translateTo	  -language to be translated
	rember language prefix
	en -> english
	es -> spanish 
	...
	"""
	from deep_translator import GoogleTranslator 
	translatedTxt = GoogleTranslator(source=writeIn, target=translateTo).translate(txt)
	return translatedTxt
def manageTranslate(writeIn,translateTo):
	try:
		translateTo[translateTo.index(writeIn)] = ""
	except:
		pass 