from Parser import FamDict,IndiDict
from datetime import datetime, date

def US09(family):
    #for each child in family:
    #check to make sure DOB is before death of both parents
    if (FamDict[family].husbandId != "N/A" and IndiDict[FamDict[family].husbandId].death != "N/A"):
        for child in FamDict[family].children: #father exists and is dead
            if(datetime.strptime(IndiDict[child].dob, '%d %b %Y') > datetime.strptime(IndiDict[FamDict[family].husbandId].death, '%d %b %Y')):
                return True #child dob is after father's death date
    if(FamDict[family].wifeId != "N/A" and IndiDict[FamDict[family].wifeId].death != "N/A"):
        for child in FamDict[family].children: #father exists and is dead
            if(datetime.strptime(IndiDict[child].dob, '%d %b %Y') > datetime.strptime(IndiDict[FamDict[family].wifeId].death, '%d %b %Y')):
                return True #child dob is after mother's death date
    return False