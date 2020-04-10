import Parser as Parser #will run Parser
from prettytable import PrettyTable
from Parser import FamDict,IndiDict,ParserErrors #now applicable
from US02 import US02
from US03 import US03
from US04 import US04
from US06 import US06
from US07 import US07
from US11 import US11
from US16 import US16
from US17 import US17
from US21 import US21
from US10 import US10
from US12 import US12
from US29 import US29
from US13 import US13
from US14 import US14
from US18 import US18
from US30 import US30
from US31 import US31 
from US15 import US15
from US19 import US19
from US05 import US05
from US08 import US08
from US35 import US35
from US36 import US36
from US37 import US37
from US01 import US01
from US09 import US09

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
print('List of Deceased:')
print(US29())
print('\n')
print('List of Living Married:')
print(US30())
print('\n')
print('List of Living Single:')
print(US31())
print('\n')
print('List of Recent Births:')
print(US35())
print('\n')
print('List of Recent Deaths:')
print(US36())
print('\n')
print('List of Recent Survivors:')
print(US37())
print('\n')


for err in ParserErrors:
    print(err)

for fam in FamDict:
    if(US13(fam)):
        print("US13 Error for Family: " + str(FamDict[fam].id) + "; Children Born Too Close Together")

    if(US04(fam)):
        print("US04 Error for Family: " + str(FamDict[fam].id) + "; Marriage Occurs After Divorce")

    if(US06(fam)):
        print("US06 Error for Family: " + str(FamDict[fam].id) + "; Divorce Occurs Before Death")

    if(US02(fam)):
        print("US02 Error for Family: " + str(FamDict[fam].id) + "; Birth of Spouse Occurs After Marriage Date")

    if(US17(fam)):
        print("US17 Error for Family: " + str(FamDict[fam].id) + "; No Marriages Between Parents and Children")

    if(US21(fam)):
        print("US21 Error for Family: " + str(FamDict[fam].id) + "; Correct Gender Roles")
    
    if(US16(fam)):
        print("US16 Annomaly for Family: " + str(FamDict[fam].id) + "; Male Last Names Within Families Match")

    if(US10(fam)):
        print("US10 Annomaly for Family: " + str(FamDict[fam].id) + "; Marriage before 14")
        
    if(US12(fam)):
        print("US12 Annomaly for Family: " + str(FamDict[fam].id) + "; Parents too old")

    if(US14(fam)):
        print("US14 Annomaly for Family: " + str(FamDict[fam].id) + "; No more than five siblings should be born at same time.")

    if(US15(fam)):
        print("US15 Annomaly for Family: " + str(FamDict[fam].id) + "; Families shouldn't have 15 or more siblings.")

    if(US19(fam)):
        print("US19 Error for Family: " + str(FamDict[fam].id) + "; First cousins cannot marry")
    
    if(US05(fam)):
        print("US05 Error for Family: " + str(FamDict[fam].id) + "; Marriage must be before death")

    if(US08(fam)):
        print("US08 Error for Family: " + str(FamDict[fam].id) + "; Children must be born during marriage(or up to 9 months after divorce)")
    
    if(US01(fam)):
        print("US01 Error for Family: " + str(FamDict[fam].id) + "; All dates must be before current date")
    
    if(US09(fam)):
        print("US09 Error for Family: " + str(FamDict[fam].id) + "; Children must be born before daeth of parents")

for indi in IndiDict:
    if(US07(indi)):
        print("US07 Annomaly for " + IndiDict[indi].name + "; Person is older than 150") 

    if(US03(indi)):
        print("US03 Error for " + IndiDict[indi].name + "; Person cannot be born after their death")

    if(US11(indi)):
        print("US11 Error for " + IndiDict[indi].name + "; Person Cannot Be Married to Two People At Once")

    if(US18(indi)):
        print("US18 Error for: " + IndiDict[indi].name + "; Siblings should not marry each other")

