import Parser as Parser
from Parser import IndiDict
from datetime import *

def US38():
	personlist=[]
	for person in IndiDict:
		personDOB= datetime.strptime(IndiDict[person].dob, '%d %b %Y')
		currentDate= datetime.now()
		d2=personDOB.replace(year=currentDate.year)
		delta=d2-currentDate
		if (delta.days>0 and delta.days<30):
			personlist.append(IndiDict[person].name)
	return personlist