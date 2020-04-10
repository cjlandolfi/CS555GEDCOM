import Parser as Parser
from Parser import IndiDict, FamDict
from datetime import *

def US37():
	personlist=[]
	for person in IndiDict:
		if not IndiDict[person].alive:
			personDOD= datetime.strptime(IndiDict[person].death, '%d %b %Y')
			currentDate= datetime.now()
			personDODPlus=personDOD+timedelta(days=30)
			if (personDODPlus>currentDate):
				if IndiDict[person].gender == 'M':
					for fam in IndiDict[person].spouse:
						if fam in FamDict:
							if not FamDict[fam].wifeName == 'N/A':
								personlist.append(FamDict[fam].wifeName)
							for child in FamDict[fam].children:
								if child in IndiDict:
									personlist.append(IndiDict[child].name)
									for grandFam in IndiDict[child].spouse:
										if grandFam in FamDict:
											for grandNameFam in FamDict[grandFam].children:
												if grandNameFam in IndiDict:
													personlist.append(IndiDict[grandNameFam].name)
				else:
					for fam in IndiDict[person].spouse:
						if fam in FamDict:
							if not FamDict[fam].husbandName == 'N/A':
								personlist.append(FamDict[fam].husbandName)
							for child in FamDict[fam].children:
								if child in IndiDict:
									personlist.append(IndiDict[child].name)
									for grandFam in IndiDict[child].spouse:
										if grandFam in FamDict:
											for grandNameFam in FamDict[grandFam].children:
												if grandNameFam in IndiDict:
													personlist.append(IndiDict[grandNameFam].name)
	return personlist