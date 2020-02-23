import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

#US06: Divorce can only occur before death of both spouses
for family in FamDict:
    if ((FamDict[family].divorce != 'N/A') and (IndiDict[FamDict[family].husbandId].alive != True) and (IndiDict[FamDict[family].wifeId].alive != True)):
        divorcedate = datetime.strptime(FamDict[family].divorce, '%d %b %Y')
        husbanddeath = datetime.strptime(IndiDict[FamDict[family].husbandId].death, '%d %b %Y')
        wifedeath = datetime.strptime(IndiDict[FamDict[family].wifeId].death, '%d %b %Y')
        if (divorcedate > husbanddeath) or (divorcedate > wifedeath):
            print("US06 Error for Family: " + str(FamDict[family].id))

#ALTERNATE VERSION
# def US06(fam):
#     if((FamDict[fam].divorce != 'N/A') and (IndiDict[FamDict[fam].husbandId].alive != True) and (IndiDict[FamDict[fam].wifeId].alive != True)):
#         divdate = datetime.strptime(FamDict[fam].divorce, '%d %b %Y')
#         husbdeath = datetime.strptime(IndiDict[FamDict[fam].husbandId].death, '%d %b %Y')
#         wifedeath = datetime.strptime(IndiDict[FamDict[fam].wifeId].death, '%d %b %Y')
#         if (divdate > husbdeath) or (divdate > wifedeath):
#             return False
#         return True

#Running the alternate version through the entire file
# for fam in FamDict:
#     if(US06(fam)==False):
#         print("US06 Error for Family: " + str(FamDict[family].id)) + " Divorce date of " 
#         + (IndiDict[FamDict[fam].husbandId].name) + " and " + (IndiDict[FamDict[fam].wifeId].name) + "occur after their deaths."
    