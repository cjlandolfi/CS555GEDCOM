import Parser as Parser
from Parser import FamDict

def US15(family):
	if (len(FamDict[family].children) >= 15):
		return True
	return False