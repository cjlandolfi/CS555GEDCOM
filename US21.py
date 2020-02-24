import Parser as Parser
from Parser import FamDict,IndiDict

def US21(family):
	#.gender
	if(FamDict[family].husbandId == "N/A" or FamDict[family].wifeId == 'N/A'):
		return False
	if(IndiDict[FamDict[family].husbandId].gender== 'N/A' or IndiDict[FamDict[family].wifeId].gender=='N/A'):
		return False
	husbandGender = IndiDict[FamDict[family].husbandId].gender
	wifeGender = IndiDict[FamDict[family].wifeId].gender
	if(husbandGender == "F") or (wifeGender == "M"):
		#print("US21 Error for Family:" + str(FamDict[family].id))
		return True
	return False
