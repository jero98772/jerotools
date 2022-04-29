#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
import os
import datetime
#import subprocess
from random import randint
months31Days = [True,"feb28",True,False,True,False,True,True,False,True,False,True]
simbols = " !#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~"

#debug functions
def p(*args,space = 5):
	"""fast print helpful in big log  p(str , [jump lines = 5])"""
	for i in args:
		print(space*"\n",i,"\n"*space)
def rnd(x):
	"""fast random number using random lib rnd(x): return random.randint(0,x)"""
	return randint(0,x)
#short functions
def lenDirInt(dirname):
	"""
	lenDirInt(directory), return int
		counts the number of folders and files in a directory """
	return len(os.listdir(dirname))
#functions
def img2NumName(dirname):
	"""
	img2NumName(dirname),return int
	returns the number of directories every 2 directories
	like , folder with 6 elements
	element0 = 0 = img2NumName(<folder with 0 elements>)
	element1 = 0 = img2NumName(<folder with 1 elements>)
	element2 = 1 = img2NumName(<folder with 2 elements>)
	element3 = 1 = img2NumName(<folder with 3 elements>)
	element4 = 2 = img2NumName(<folder with 4 elements>)
	element5 = 2 = img2NumName(<folder with 5 elements>)
	"""
	try:
		lendir = lenDirInt(dirname)
		if lendir % 2 == 0:
			return lendir/2
		else :
			return (lendir-1)/2
	except:
		lendir = 0
	return lendir
#useful functions
def mayor(num1,num2):
	"""return higher number , of 2 numbers, mayor(num1,num2)"""
	if num1>num2:
		return num1
	else:
		return num2
def menor(num1,num2):
	"""return least number , of 2 numbers, menor(num1,num2)"""
	if num1<num2:
		return num1
	else:
		return num2
def mismaContraseña(password1,password2):
	"""mismaContraseña(password1,password2) return bool
		if are same password of arg 1 and arg 2 , return True if are diferent return False"""
	if password1 == password2:
		return True
	else:
		return False
def minCaracteresPass(password,cantidad):
	"""minCaracteresPass(password,cantidad); return bool
	 is to see if a password meets minimum characters  return True else False """
	if len(password) > cantidad:
		return True
	else:
		return False
def contraseñaSegura(password):
	"""
	contraseñaSegura(str), return True if str have numbers ,strings and symbols else return False
	"""
	haynumeros = False
	hayletras = False
	haysimbolos = False
	numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in password:
		try:
			if i in numeros:
				haynumeros = True
			elif i in letras:
				hayletras = True
			else:
				if type(int(i)) == type(0):
					haynumeros = True
				elif type(str(i)) == type(""):
					hayletras = True				
		except:
			haysimbolos = True
	if haysimbolos and hayletras and haynumeros:
		return True
	else:
		return False
def camposVacios(userName,password1,password2,email,date):
	"""camposVacios(userName,password1,password2,email,date) ,return bool ,if args = "" """
	if userName == "" and password1 == "" and password2 == "" and email == "" and date == "":
		return False
	else:
		return True
def campoVacio(text):
	"""campoVacio(text), return True if text = '' else False"""
	if text == "":
		return True
	else: 
		return False
def esCorreo(email):
	"""esCorreo(string) ,return True if string have '.' and '@'"""
	if "@" in email and "." in email:
		return True
	else:
		return False
def generatePassword():
	"""generatePassword(),return srtring
	generate random string 
	"""
	genPassowrd = ""
	for i in range(0,16):
		if len(genPassowrd) >= 16 and len(genPassowrd)-len(hexStr) <= 16:
			num = rnd.randint(0,9999)
			if 32 > num >126:
				char = chr(num)
				genPassowrd += char
			else:
				hexStr = str(hex(hexStr))
				genPassowrd += hexStr
		else:
			break
	return genPassowrd
def deleteFile(path):
	"""
	deleteFish(path) , delete a img of fish ,for data_basecsv
	"""
	if os.path.isfile(path) :			
		os.remove(path)
def deleteWithExt(path,ext):
	"""
	deleteWithExt(<file path>,<file extencion>) , delete file with file extencion
	"""
	if os.path.isfile(path+ext) :			
		os.remove(path+ext)
def deletefiles(path):
	"""
	deletefiles(path) , delete records of pandemaths
	"""
	#get 
	files=os.listdir(path)
	for i in files:
		if os.path.isfile(path+i):
			os.remove(path+i)
def readtxtline(name):
	"""
	readtxtline(name), return frist line of file as string
	"""
	with open(name, 'r') as file:
		return str(file.readline())
def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
def readfilelist(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content
def readtxtstr(name):
	"""
	readtxtstr(name) , return txt content as string
	"""
	content = ""
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content += str(i).replace("\n","")
	return content
def readfilestr(name):
	"""
	readtxtstr(name) , return txt content as string
	"""
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content += str(i).replace("\n","")
	return content
def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	content =str(content)
	with open(name+".txt", 'w') as file:
		file.write(content)
		file.close()
def yesno(msg):
	"""
	yesno(msg) ,if msg == yes return True else return False 
	"""
	if msg.lower() == "yes":
		return True
	elif msg.lower() == "no":
		return False
def isEmpty(*args):
	"""
	isEmpty(*args), return True if all variable are filled
	"""
	for i in args:
		if i != "":
			return True  
		else:
			return False
			break
def allReplaceSimbols(txt):
	"""
	allReplaceSimbols(<string>) ,if have any delelte simbol that , return  string as integer
	"""
	for i in simbols:
		if i in txt:
			txt = txt.replace(i,"")
	return int(txt)
def date2int(date):
	"""
	date2int(date) convert date to int
	"""
	date = str(date)
	intdate = date.replace(":","").replace("/","").replace(",","").replace(" ","")
	return int(intdate)
def limitsize(size,limit):
	"""
	limitsize(size,limit) return size if greater than limit return new size  
	"""
	size = int(size)
	if size < int(limit):
		return size
	else:
		return int(size/len(str(size)))
def setLimit(value,limit):
	"""
	setLimit(value,limit) , return value or limit value
	"""
	if value < limit:
		return value
	else:
		return limit
def getExt(filename):
	"""
	getExt(filename) return extecion of file 
	"""
	isPoint = False
	for i in str(filename):
		if i == ".":
			ext = "."
			isPoint = True
		elif isPoint:
			if i == "'":
				break
			ext += i
	return ext

def concatenateStrInList(arr):
	"""
	concatenates the numbers of a string, the elements of an array : return  integer
	"""
	intAsString = ""
	for i in arr:
		intAsString += i
	return int(intAsString)
def linkedlistfile(name,old,new,option = "ab+",replaceTo="<!--this-->"):
	oldString = replaceTo+old+replaceTo
	newString = replaceTo+new+replaceTo
	newContent = readFile(name).replace(oldString,newString)
	#add integrate a main.py
	writeTxt(name,newContent,option="w")
def htmlInit(name,content):
	return f"""
<!DOCTYPE html>
<html lang="en">
	<meta charset="UTF-8"> 
	<head>
		<title>blog {name}</title>
	</head>
	<body>
			<h1>{name}</h1>
			<br>
		<center>
			<hr>
			{content}
		</center>
	</body>
</html>
	"""
def htmltxt(txtp:str,txtq:str,id:str,who:str)->str:
	"""
	htmltxt(txtp:str,txtq:str,id:str,who:str)->str
	generate html code for a blog entry in B-feelLog
	"""
	now = time.ctime()
	return f"""
<div id="{id}">
<h2>{txtp}</h2>
<br>
<table width = "420">
	<tr>
		<td>
			<p>{txtq}</p>
		</td>
	</tr>
</table>
<p>{now},by {who}.</p>
</div>
<hr>
"""

def readRealtime(name:str,sep=";":str):
  """
  readRealtime(name:str,sep=";":str)) , is a genteretor return row of csv at iteration 
  """
  with open(name, 'r') as file:
    for i in file.readlines():
      yield i.split(sep)
