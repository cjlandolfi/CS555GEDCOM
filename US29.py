import Parser as Parser
from Parser import IndiDict

def US29():
	personlist=[]
	for person in IndiDict:
		if not IndiDict[person].alive:
			personlist.append(IndiDict[person].name)
	return personlist