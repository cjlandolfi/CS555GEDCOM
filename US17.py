import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

def US17(family):
	if (FamDict[family].husbandId == 'N/A' or FamDict[family].wifeId == 'N/A'):
		return False
	if FamDict[family].wifeId in FamDict[family].children or FamDict[family].husbandId in FamDict[family].children:
		return True
	elif IndiDict[FamDict[family].husbandId].child in FamDict:
		if FamDict[family].wifeId == FamDict[IndiDict[FamDict[family].husbandId].child].wifeId:
			return True
	elif IndiDict[FamDict[family].wifeId].child in FamDict:
		if FamDict[family].husbandId == FamDict[IndiDict[FamDict[family].wifeId].child].husbandId:
			return True
	return False