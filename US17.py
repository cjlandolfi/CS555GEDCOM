import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

for family in FamDict:
	if FamDict[family].wifeId in FamDict[family].children or FamDict[family].husbandId in FamDict[family].children:
		print("US17 Error for Family:" + str(FamDict[family].id))
	elif IndiDict[FamDict[family].husbandId].child in FamDict:
		if FamDict[family].wifeId == FamDict[IndiDict[FamDict[family].husbandId].child].wifeId:
			print("US17 Error for Family:" + str(FamDict[family].id))
	elif IndiDict[FamDict[family].wifeId].child in FamDict:
		if FamDict[family].husbandId == FamDict[IndiDict[FamDict[family].wifeId].child].husbandId:
			print("US17 Error for Family:" + str(FamDict[family].id))