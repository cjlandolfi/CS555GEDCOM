from Parser import FamDict,IndiDict
from datetime import datetime, date

def US05(family):
    if (FamDict[family].married == 'N/A' or FamDict[family].husbandId == "N/A" or FamDict[family].wifeId == "N/A"):
        return False
    else:
        marriageDate = datetime.strptime(FamDict[family].married, '%d %b %Y')
        husbandDob = datetime.strptime(IndiDict[FamDict[family].husbandId].dob, '%d %b %Y')
        wifeDob = datetime.strptime(IndiDict[FamDict[family].wifeId].dob, '%d %b %Y')

        if marriageDate > husbandDob or marriageDate > wifeDob:
            return True
        else:
            return False