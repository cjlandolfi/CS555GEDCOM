from Parser import FamDict,IndiDict

def US12(family):
    if(FamDict[family].children == [] or FamDict[family].husbandId == "N/A" or FamDict[family].wifeId == "N/A"):
        return False
    husbandAge = IndiDict[FamDict[family].husbandId].age
    wifeAge = IndiDict[FamDict[family].wifeId].age
    for child in FamDict[family].children:
        childAge = IndiDict[child].age
        if((wifeAge - childAge >= 60) or (husbandAge - childAge >= 80)):
            return True
    return False