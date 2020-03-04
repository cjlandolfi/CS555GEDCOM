import Parser as Parser #will run Parser
from prettytable import PrettyTable
from Parser import FamDict,IndiDict #now applicable
from US02 import US02
from US03 import US03
from US04 import US04
from US06 import US06
from US07 import US07
from US11 import US11
from US16 import US16
from US17 import US17
from US21 import US21

#Import All Checks (User Stories)

indiTable = PrettyTable()
indiTable.field_names = ["ID", "Name", "Gender", "DOB", "Age", "Alive", "Death", "Child", "Spouse"]

famTable = PrettyTable()
famTable.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]

for key in IndiDict:
    indiTable.add_row([key, IndiDict[key].name, IndiDict[key].gender, IndiDict[key].dob, IndiDict[key].age, IndiDict[key].alive, IndiDict[key].death, IndiDict[key].child, IndiDict[key].spouse])

for key in FamDict:
    famTable.add_row([key, FamDict[key].married, FamDict[key].divorce, FamDict[key].husbandId, FamDict[key].husbandName, FamDict[key].wifeId, FamDict[key].wifeName, FamDict[key].children])

print('Individuals')
print(indiTable)
print('\n')
print('Families')
print(famTable)
print('\n')

for fam in FamDict:
    if(US04(fam)):
        print("US04 Error for Family: " + str(FamDict[fam].id) + "; Marriage Occurs After Divorce")

    if(US06(fam)):
        print("US06 Error for Family: " + str(FamDict[fam].id) + "; Divorce Occurs Before Death")

    if(US02(fam)):
        print("US02 Error for Family:" + str(FamDict[fam].id) + "; Birth of Spouse Occurs After Marriage Date")

    if(US17(fam)):
        print("US17 Error for Family:" + str(FamDict[fam].id) + "; No Marriages Between Parents and Children")

    if(US21(fam)):
        print("US21 Error for Family:" + str(FamDict[fam].id) + "; Correct Gender Roles")
    
    if(US16(fam)):
        print("US16 Annomaly for Family:" + str(FamDict[fam].id) + "; Male Last Names Within Families Match")

for indi in IndiDict:
    if(US07(indi)):
        print("US07 Annomaly for " + IndiDict[indi].name + "; Person is older than 150") 

    if(US03(indi)):
        print("US03 Error for " + IndiDict[indi].name + "; Person cannot be born after their death")

    if(US11(indi)):
        print("US11 Error for " + IndiDict[indi].name + "; Person Cannot Be Married to Two People At Once")