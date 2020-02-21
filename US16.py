import Parser as Parser
from Parser import FamDict,IndiDict

for family in FamDict:
	husbandName=IndiDict[FamDict[family].husbandId].name
	lastName=husbandName.split()
	for child in FamDict[family].children:
		if(IndiDict[child].gender =="M"):
			childName= IndiDict[child].name
			childLast= childName.split()
			if (lastName[1] != childLast[1]):
				print("US16 Error for Family:" + str(FamDict[family].id))