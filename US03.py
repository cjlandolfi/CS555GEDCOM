import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

for person in IndiDict:
	print(person.alive)
	if not IndiDict[person].alive:
		birthDate = datetime.strptime(IndiDict[person].dob, '%d %b %Y')
		deathDate = datetime.strptime(IndiDict[person].death, '%d %b %Y')
		if (deathDate < birthDate):
			print("US03 Error for " + str(IndiDict[person].name))