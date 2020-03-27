from Parser import FamDict,IndiDict
from datetime import datetime, date

def US05(family):
    marriageDate = datetime.strptime(FamDict[family].married, '%d %b %Y')
    husbandDob = datetime.strptime(IndiDict[FamDict[family].husbandId].dob, '%d %b %Y')
    wifeDob = datetime.strptime(IndiDict[FamDict[family].wifeId].dob, '%d %b %Y')

    if marriageDate.days >= husbandDob.days or marriageDate.days >= wifeDob.days:
        return True
    else:
        return False