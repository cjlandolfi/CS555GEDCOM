from Parser import FamDict,IndiDict
from datetime import datetime, date

def US08(family):
    for child in FamDict[family].children:
        #check if person dob is before parent marriage
        if IndiDict[child].dob.days < FamDict[family].marriage.days:
            return True
        elif FamDict[family].divorce != "N/A":
            divorceDate = datetime.strptime(FamDict[family].divorce, '%d %b %Y')
            childDob = datetime.strptime(IndiDict[child].dob, '%d %b %Y')
            if (abs(divorceDate.month - childDob.month) > 9):
                return True
        else:
            return False