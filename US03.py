import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

def US03(person):
	if not IndiDict[person].alive:
		birthDate = datetime.strptime(IndiDict[person].dob, '%d %b %Y')
		deathDate = datetime.strptime(IndiDict[person].death, '%d %b %Y')
		if (deathDate < birthDate):
			return True
		return False
	return False