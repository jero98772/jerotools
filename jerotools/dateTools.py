def fechaStr2Arr(fecha):
	"""
	fechaStr2Arr(<date as string>) , return date as array
	convert date to array
	"""
	fechaArr = []
	tmp = ""
	for i in str(fecha):
		if i == "," or i == "-" or i == ":" or i =="/":
			fechaArr.append(tmp)
			tmp = ""
		else :
			tmp += i
	else: 
		fechaArr.append(tmp)
	return fechaArr
def hay29feb(año):
	"""
	hay29feb(Yeard) 
	if that yeard have 29 of February,return True"""
	if año % 4 == 0:
		feb29Booll  = True
	else :
		feb29Booll  = False
	return feb29Booll
def dias29feb(años):
	"""
	dias29feb(yeard), return yeard // 4
		to add up the years with February 29
	"""
	diasX29feb = años // 4
	return  diasX29feb 
def dias2mes(dias):
	"""
	dias2mes(<numbers of days>):return months 
		how many days in a number of months
	"""
	meses = 0
	i = 0
	while mes >= i :
		mesI = i%12
		if esMesesCon31dias[30+mesI] == 31:
			meses += 1
		elif esMesesCon31dias[30-2] == "feb28":
			meses += 1
		else:
			meses += 1
		i+=1
	return meses
def meses2Dias(mes):
	"""
	meses2Dias(months): return days
		quantity days have that month 31,30,28...29  
	"""
	dias = 0
	i = 0
	while mes >= i :
		mesI = i%12
		if esMesesCon31dias[mesI]:
			dias += 31
		elif esMesesCon31dias[mesI] == "feb28":
			dias += 28
		else:
			dias += 30
		i+=1
	return dias
def hoyArr():
	"""
	return date as array
	"""
	hoy = fechaStr2Arr(str(datetime.datetime.today().strftime('%Y-%m-%d')))
	return hoy
def hoyStr():
	"""
	return date as string
	"""
	hoy = str(datetime.datetime.today().strftime('%Y-%m-%d'))
	return hoy
def hoyminsArr():
	"""
	return date and hours and minutes as array
	"""
	hoy = fechaStr2Arr(datetime.datetime.today().strftime("%m/%d/%Y, %H:%M"))
	return hoy
def hoyminsStr():
	"""
	return date and hours and minutes as string
	"""
	hoy = datetime.datetime.today().strftime("%m/%d/%Y, %H:%M")
	return hoy

def diasTotales(dia):
	"""
	diasTotales(<date with days ,months and yeards as array[yeards,months,days]>)
	return total days of date
	"""
	años = int(dia[0])
	añosTotales = años * 365
	meses = int(dia[1])
	dias = int(dia[2])
	diasDeMeses = meses2Dias(meses)
	if años == 0:
		diasTotales =  diasDeMeses + dias
	else:	
		dias += dias29feb(años)
		diasTotales = añosTotales + dias + diasDeMeses 
	return diasTotales
def minsTotales(dia):
	"""
	diasTotales(<date and hours and minutes >)
	return total minute of date	
	"""
	#fechaStr2Arr(dia)
	diasTotalesVar = diasTotales(dia[:3])
	minsTotales = (((diasTotalesVar)*24)+int(dia[3])*60)+int(dia[4]) 
	return minsTotales	
def diferneciaFecha(date,date2):
	"""
	diferneciaFecha(date,date2)
	return difference of days of the 2 dates as int
	"""
	date = diasTotales(date)
	date2 = diasTotales(date2)
	if date2 > date:
		difference= date2 - date 
	else:
		difference = date - date2
	return difference
def Mas1Dia(lastDate):
	"""
	Mas1Dia(<date>)
	return True if date is different to date now
	"""
	newDate = hoyArr()
	difference = diferneciaFecha(lastDate,newDate)
	if difference == 0 :
		return True
	else:
		return False


def olderDate2(date,date2):
	"""
	olderDate2(date,date2)
	return older date in format  ,input in format "yyyymmdd"
	"""
	date = str(date)
	date2 = str(date2)
	if date < date2:
		return date
	else:
		return date2
def latestDate2(date,date2):
	"""
	latestDate2(date,date2)
	return latest date ,input in format "yyyymmdd"
	"""
	date = str(date)
	date2 = str(date2)
	if date > date2:
		return date
	else:
		return date2
def latestDate(*dates):
	"""
	latestDate(*dates)
	return latest in format ,input in format "yyyymmdd"
	"""
	selectedDate=""
	for i in dates:
		if selectedDate > i:
			selectedDate= i
	return selectedDate
def olderDate(*dates):
	"""
	olderDate(*date)
	return older date in format ,input in format "yyyymmdd"
	"""
	selectedDate=""
	for i in dates:
		if selectedDate < i:
			selectedDate= i
	return selectedDate