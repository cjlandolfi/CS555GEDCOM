import Parser as Parser
from Parser import FamDict,IndiDict

#US14: No more than five siblings should be born at same time.
def US14(fam):
    if (len(FamDict[fam].children) < 5):
        return False
    else:
        siblingBdays = {}
        for sibling in FamDict[fam].children:
            for person in IndiDict:
                if sibling == IndiDict[person].id:
                    if IndiDict[person].dob in siblingBdays:
                        siblingBdays[IndiDict[person].dob] += 1
                        if siblingBdays[IndiDict[person].dob] >= 5:
                            return True
                    else:
                        siblingBdays[IndiDict[person].dob] = 1
        return False

