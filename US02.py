from Parser import FamDict,IndiDict
from datetime import datetime, date

def US02(family):
    if (FamDict[family].husbandId == 'N/A' or FamDict[family].wifeId == 'N/A'):
        return False
    if (IndiDict[FamDict[family].husbandId].dob == 'N/A' or IndiDict[FamDict[family].wifeId].dob == 'N/A' or FamDict[family].married == 'N/A'):
        return False
    mardate = datetime.strptime(FamDict[family].married, '%d %b %Y')
    husbbirth = datetime.strptime(IndiDict[FamDict[family].husbandId].dob, '%d %b %Y')
    wifebirth = datetime.strptime(IndiDict[FamDict[family].wifeId].dob, '%d %b %Y')
    if (husbbirth > mardate) or (wifebirth > mardate):
        return True
    else: 
        return False