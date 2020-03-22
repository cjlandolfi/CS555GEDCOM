import Parser as Parser
from Parser import IndiDict

#US31: List living single
def US31():
    singlelist = []
    for person in IndiDict:
        if IndiDict[person].alive:
            if IndiDict[person].spouse == []:
                singlelist.append(IndiDict[person].name)
    return singlelist