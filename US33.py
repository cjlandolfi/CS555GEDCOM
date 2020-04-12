import Parser as Parser
from Parser import IndiDict
from Parser import FamDict

#US33: List all orphans
def US33():
    orphanlist = []
    for person in IndiDict:
        if IndiDict[person].child == 'N/A' and IndiDict[person].spouse != []:
            for famid in IndiDict[person].spouse:
                if FamDict[famid].married != 'N/A':
                    if FamDict[famid].husbandId == 'N/A' or FamDict[famid].wifeId == 'N/A':
                        continue
                    husband = FamDict[famid].husbandId
                    wife = FamDict[famid].wifeId
                    if IndiDict[FamDict[famid].husbandId].death != 'N/A' and IndiDict[FamDict[famid].wifeId].death != 'N/A':
                        for child in FamDict[famid].children:
                            if IndiDict[child].age < 18:
                                orphanlist.append(IndiDict[child].name)
    orphanlist = list(dict.fromkeys(orphanlist))
    return orphanlist