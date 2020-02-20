import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

for family in FamDict:
    mardate = datetime.strptime(FamDict[family].married, '%d %b %Y')
    husbbirth = datetime.strptime(IndiDict[FamDict[family].husbandId].dob, '%d %b %Y')
    wifebirth = datetime.strptime(IndiDict[FamDict[family].wifeId].dob, '%d %b %Y')
    if (husbbirth > mardate) or (wifebirth > mardate):
        print("US02 Error for Family:" + str(FamDict[family].id))