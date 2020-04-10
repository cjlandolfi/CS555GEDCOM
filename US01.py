from Parser import FamDict,IndiDict
from datetime import datetime, date

def US01(family):
    #dates before current date
    currentDate = datetime.today()
    if (FamDict[family].married != "N/A" and (datetime.strptime(FamDict[family].married, '%d %b %Y') > currentDate)):
        return True #marriage date exists and is after current date
    if (FamDict[family].divorce != "N/A"and (datetime.strptime(FamDict[family].divorce, '%d %b %Y') > currentDate)):
        return True #divorce date exists and is after current date
    if (FamDict[family].husbandId != "N/A" and (datetime.strptime(IndiDict[FamDict[family].husbandId].dob, '%d %b %Y') > currentDate)):
        return True #husband exists and DOB is after current date
    if (FamDict[family].husbandId != "N/A" and IndiDict[FamDict[family].husbandId].death != "N/A" and (datetime.strptime(IndiDict[FamDict[family].husbandId].death, '%d %b %Y') > currentDate)):
        return True #husband exists and is dead and death date is after current date
    if (FamDict[family].husbandId != "N/A" and (datetime.strptime(IndiDict[FamDict[family].wifeId].dob, '%d %b %Y') > currentDate)):
        return True #wife exists and is after current date
    if (FamDict[family].husbandId != "N/A" and IndiDict[FamDict[family].wifeId].death != "N/A" and (datetime.strptime(IndiDict[FamDict[family].wifeId].death, '%d %b %Y') > currentDate)):
        return True #wife exists and is dead and death date is after current date
    for child in FamDict[family].children:
        if datetime.strptime(IndiDict[child].dob, '%d %b %Y') > currentDate:
            return True #child DOB is after current date
        if IndiDict[child].death != "N/A" and datetime.strptime(IndiDict[child].death, '%d %b %Y') > currentDate:
            return True #child is dead and death date is after current date
    return False #no dates are after current date