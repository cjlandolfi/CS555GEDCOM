import Parser as Parser
from Parser import IndiDict
from datetime import *

def US36():
	personlist=[]
	for person in IndiDict:
		if not IndiDict[person].alive:
			personDOD= datetime.strptime(IndiDict[person].death, '%d %b %Y')
			currentDate= datetime.now()
			personDODPlus=personDOD+timedelta(days=30)
			if (personDODPlus>currentDate):
				personlist.append(IndiDict[person].name)
	return personlist