import Parser as Parser
from Parser import IndiDict
from datetime import *

def US35():
	personlist=[]
	for person in IndiDict:
		personDOB= datetime.strptime(IndiDict[person].dob, '%d %b %Y')
		currentDate= datetime.now()
		personDOBPlus=personDOB+timedelta(days=30)
		if (personDOBPlus>currentDate):
			personlist.append(IndiDict[person].name)
	return personlist