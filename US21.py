import Parser as Parser
from Parser import FamDict,IndiDict

for family in FamDict:
	#.gender
	husbandGender = IndiDict[FamDict[family].husbandId].gender
	wifeGender = IndiDict[FamDict[family].wifeId].gender
	if(husbandGender == "F") or (wifeGender == "M"):
		print("US21 Error for Family:" + str(FamDict[family].id))