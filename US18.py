import Parser as Parser
from Parser import FamDict,IndiDict

#US18: Siblings should not marry each other.
def US18(person):
    if(IndiDict[person].spouse == []):
        return False
    
    for sibling in IndiDict:
        if(((IndiDict[person].child and IndiDict[sibling].child) != "N/A" and IndiDict[person].child == IndiDict[sibling].child and (IndiDict[person].id != IndiDict[sibling].id) and (not set(IndiDict[person].spouse).isdisjoint(IndiDict[sibling].spouse)))):
            return True
    return False