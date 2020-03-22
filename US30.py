import Parser as Parser
from Parser import IndiDict

#US30: List living married
def US30():
    marriedlist=[]
    for person in IndiDict:
        if IndiDict[person].alive:
            if IndiDict[person].spouse != []:
                marriedlist.append(IndiDict[person].name)
    return marriedlist