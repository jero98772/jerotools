
from flask import request,render_template_string
def multrequest(items):
	"""save request in array  """
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
def distributedWebWithIframe(url,direccions,webApp,runWeb):
	"""replace webpage with iframe to same page in other server"""
	for webroute in direccions:		
		print(webroute)
		@webApp.route(url+str(webroute)+".html", endpoint=webroute , methods=['GET','POST'])
		def site():
			return render_template_string("{% extends  '"+url+"template.html'%}{% block content %}<iframe src='"+str(runWeb)+url+str(webroute)+".html#webContent"+"' scrolling='no' class='frameDistrution'> </iframe> {% endblock %}")
		return site()