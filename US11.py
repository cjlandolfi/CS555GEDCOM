import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

def US11(person):
	for fam in IndiDict[person].spouse:
		for fam2 in IndiDict[person].spouse:
			if fam == fam2:
				continue
			if not (fam in FamDict or fam2 in FamDict):
				continue
			if FamDict[fam].divorce == 'N/A' or FamDict[fam2].married == 'N/A':
				continue
			fam1end = datetime.strptime(FamDict[fam].divorce, '%d %b %Y')
			fam2start = datetime.strptime(FamDict[fam2].married, '%d %b %Y')
			if (fam2start < fam1end):
				return True
	return False