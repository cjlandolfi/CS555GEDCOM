import Parser as Parser
from Parser import FamDict,IndiDict

def US19(family):
	if (FamDict[family].husbandId == 'N/A' or FamDict[family].wifeId == 'N/A'):
		return False
	if FamDict[family].wifeId in IndiDict and FamDict[family].husbandId in IndiDict:
		if IndiDict[FamDict[family].wifeId].child in FamDict and IndiDict[FamDict[family].husbandId].child in FamDict:
			if FamDict[IndiDict[FamDict[family].wifeId].child].husbandId in IndiDict and FamDict[IndiDict[FamDict[family].husbandId].child].husbandId in IndiDict:
				if IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].husbandId].child in FamDict and IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].husbandId].child in FamDict:
					if FamDict[IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].husbandId].child] == FamDict[IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].husbandId].child]:
						return True #if husband and wife's fathers were siblings
			elif FamDict[IndiDict[FamDict[family].wifeId].child].wifeId in IndiDict and FamDict[IndiDict[FamDict[family].husbandId].child].wifeId in IndiDict:
				if IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].wifeId].child in FamDict and IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].wifeId].child in FamDict:
					if FamDict[IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].wifeId].child] == FamDict[IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].wifeId].child]:
						return True #if husband and wife's mothers were siblings
			elif FamDict[IndiDict[FamDict[family].wifeId].child].husbandId in IndiDict and FamDict[IndiDict[FamDict[family].husbandId].child].wifeId in IndiDict:
				if IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].husbandId].child in FamDict and IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].wifeId].child in FamDict:
					if FamDict[IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].husbandId].child] == FamDict[IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].wifeId].child]:
						return True #if wife's father and husband's mother were siblings
			elif FamDict[IndiDict[FamDict[family].wifeId].child].wifeId in IndiDict and FamDict[IndiDict[FamDict[family].husbandId].child].husbandId in IndiDict:
				if IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].wifeId].child in FamDict and IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].husbandId].child in FamDict:
					if FamDict[IndiDict[FamDict[IndiDict[FamDict[family].wifeId].child].wifeId].child] == FamDict[IndiDict[FamDict[IndiDict[FamDict[family].husbandId].child].husbandId].child]:
						return True #if wife's mother and husband's father were siblings
	return False