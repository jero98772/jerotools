#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
from flask import request,render_template_string
def multrequest(items):
	"""save request in array  
	:param arg: parametro
    :type arg:list 
        :return: retorno
        :rtype: (tipo de dato al retonar)
	"""
	values = []
	for item in items:		
		item = request.form.get(item)
		try:
			item = float(item)
		except:	
			item = str(item)
		values.append(item)
	return values
def multrequestStr(items):
	"""save request in array as string """	
	values = []
	for item in items:		
		item = str(request.form.get(item))
		values.append(item)
	return values
def joinWebpage(url,direccions,webApp,acualapp):
	"""merge 2 flask apps in one"""
		for webroute in direccions:		
			@acualapp.route(url+str(webroute)+".html", endpoint=webroute , methods=['GET','POST'])
			def site():
				return webApp
		return site()
def distributedIframe(url,direccions,webApp,runWeb):
	"""replace webpage with iframe to same page in other server (only works in flask)"""
	for webroute in direccions:		
		print(webroute)
		@webApp.route(url+str(webroute)+".html", endpoint=webroute , methods=['GET','POST'])
		def site():
			return render_template_string("{% extends  '"+url+"template.html'%}{% block content %}<iframe src='"+str(runWeb)+url+str(webroute)+".html#webContent"+"' scrolling='no' class='frameDistrution'> </iframe> {% endblock %}")
		return site()
def addtemplatehtml(name,content,option = "ab+",replaceTo="<!--addition-->"):
	if content == "":
		initTemplate = "{% extends  'template.html'%}{% block content %}"
		endTemplate = "{% endblock %}"
		content = initTemplate+content+replaceTo+endTemplate
		newContent =  content 
	else:
		newContent = readFile(name).replace(replaceTo,content+replaceTo)
	writeTxt(name,newContent,option="w")
def genwebsint(dirs,dataDir,classname="webcontets"):
    newCode = """from flask import Flask, render_template
app = Flask(__name__)
class """+classname+"""():"""
    for i in dirs:
        newCode += addweb(i)
    writeTxt(dataDir,newCode,"w")
def addweb(name,path="",category=""):
	txt = f'\n\t@app.route("{category}/{name}")\n\tdef {str(name[:-5]).replace("/","")}():\n\t\treturn render_template("{category}/{name}")'
	return txt