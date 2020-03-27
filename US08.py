from Parser import FamDict,IndiDict
from datetime import datetime, date

def US08(family):
    for child in FamDict[family].children:
        if FamDict[family].married != "N/A":
            marriageDate = datetime.strptime(FamDict[family].married, '%d %b %Y')
            childDob = datetime.strptime(IndiDict[child].dob, '%d %b %Y')
            #check if person dob is before parent marriage
            if childDob < marriageDate:
                return True
            elif FamDict[family].divorce != "N/A":
                divorceDate = datetime.strptime(FamDict[family].divorce, '%d %b %Y')

                if (abs((divorceDate - childDob).days) > 270):
                    return True
            else:
                return False