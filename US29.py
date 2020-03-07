import Parser as Parser
from Parser import IndiDict

def US29():
	for person in IndiDict:
		if not IndiDict[person].alive:
			print(IndiDict[person].name)