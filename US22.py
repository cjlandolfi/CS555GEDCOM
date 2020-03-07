import Parser as Parser
from Parser import FamDict,IndiDict

def US22():
	count = 0
	for fam in FamDict:
		for fam2 in FamDict:
			if fam == fam2:
				count = count + 1
		if count > 1:
			return True
		else:
			count = 0
	for indi in IndiDict:
		for indi2 in IndiDict:
			if indi == indi2:
				count = count + 1
		if count > 1:
			return True
		else:
			count = 0
	return False