import Parser as Parser
from Parser import IndiDict,FamDict

def US28(family):
	myChildList={}
	x=[]
	for child in FamDict[family].children:
		childtag=str(child)
		childage=IndiDict[child].age
		myChildList.update({childtag:childage})
	print(myChildList)
	for m,value in sorted(myChildList.items(),key=lambda item:item[1]):
		x.append(m)
	return x