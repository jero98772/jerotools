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
def noaaResample(name:str):
	"""
	noaaResample(name:str)->imagefilename 
	with a wav file obteined of noaas satelite generate a png file using hilbert transform,resampled is better cuality, sometimes audio not was resample
	"""
	import scipy.io.wavfile as wav
	import scipy.signal as signal
	import numpy as np
	from PIL import Image
	import matplotlib.pyplot as plt
	import datetime
    fs, data = wav.read(SAVESFOLDER+name)  
    data_crop = data[20*fs:21*fs]
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 4*h))
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.savefig(IMGFOLDER+filename)
    return filename
def noaa(name:str):
	"""
	noaaResample(name:str)->imagefilename 
	with a wav file obteined of noaas satelite generate a png file using hilbert transform
	"""
	import scipy.io.wavfile as wav
	import scipy.signal as signal
	import numpy as np
	from PIL import Image
	import matplotlib.pyplot as plt
	import datetime
    fs, data = wav.read(SAVESFOLDER+name)  
    data_crop = data[20*fs:21*fs]
    resample = 4
    data = data[::resample]
    fs = fs//resample
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:

            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 4*h))
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.savefig(IMGFOLDER+filename)
    return filename
def markovchain(data:dict,times=1,start=None)->list:
	"""
	markovchain(data:dict,times=1,start=None)->list
	generate markov chain
	"""
	import random
	values=[]
	value=start
	for i in range(times):
		value=random.choices(list(data.keys()),weights=data[value],k=1)	
		value=value[0]	
		values.append(value)
	return values
def getprob(l:list)->dict:
	"""
	getprob(l:list)->dict
	get proabiliti of ocurrences in list
	"""
	clearlist=list(set(l))
	prob={}
	for i in clearlist:
		prob[str(i)]=l.count(i)/len(l)
	return prob
def distribution(data:dict,times=1)->list:
	"""
	distribution(data:str,times=1)->list
	generate proabiliti distribution with elements of dictionary
	"""
	import random
	values=[]
	for i in range(times):
		value=random.choices(list(data.keys()),weights=data[value],k=1)	
		value=value[0]	
		values.append(value)
	return values	