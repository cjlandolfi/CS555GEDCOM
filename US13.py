import Parser as Parser
from Parser import IndiDict,FamDict
from datetime import datetime, date

def US13(family):
	if(FamDict[family].children=='N/A'):
		return False
	for child in FamDict[family].children:
		dobCurrent=datetime.strptime(IndiDict[child].dob, '%d %b %Y')
		for children in FamDict[family].children:
			dobChildren=datetime.strptime(IndiDict[children].dob, '%d %b %Y')
			change=abs(dobCurrent-dobChildren)
			if(change.days>1 and change.days<244):
				return True
	return False