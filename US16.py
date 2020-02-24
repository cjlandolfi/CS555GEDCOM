import Parser as Parser
from Parser import FamDict,IndiDict

def US16(family):
	if(FamDict[family].husbandId =="N/A"):
		return False
	if(IndiDict[FamDict[family].husbandId].name == 'N/A'):
		return False
	husbandName=IndiDict[FamDict[family].husbandId].name
	lastName=husbandName.split()
	for child in FamDict[family].children:
		if(IndiDict[child].gender =="N/A" or IndiDict[child].name =="N/A"):
			return False
		if(IndiDict[child].gender =="M"):
			childName= IndiDict[child].name
			childLast= childName.split()
			if (lastName[1] != childLast[1]):
				return True
	return False