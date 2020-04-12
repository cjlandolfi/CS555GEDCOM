import Parser as Parser
from Parser import IndiDict
from Parser import FamDict
from datetime import datetime, date

#US34: List large age differences
def US34():
    couplelist = []
    for fam in FamDict:
        if FamDict[fam].married != "N/A":
            marriagedate = datetime.strptime(FamDict[fam].married, '%d %b %Y')
            if (FamDict[fam].husbandId == "N/A" or FamDict[fam].wifeId == "N/A"):
                continue
            husbandDOB = datetime.strptime(IndiDict[FamDict[fam].husbandId].dob, '%d %b %Y') 
            wifeDOB = datetime.strptime(IndiDict[FamDict[fam].wifeId].dob, '%d %b %Y')
            husbandAgeAtMarriage = marriagedate - husbandDOB
            wifeAgeAtMarriage = marriagedate - wifeDOB

            if((husbandAgeAtMarriage > (2 * wifeAgeAtMarriage)) or (wifeAgeAtMarriage > (2 *husbandAgeAtMarriage))):
                couplename = IndiDict[FamDict[fam].husbandId].name + " and " + IndiDict[FamDict[fam].wifeId].name
                couplelist.append(couplename)
    return couplelist
