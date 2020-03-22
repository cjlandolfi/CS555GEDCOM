from datetime import datetime, date

GEDCOM = open("test.ged", "r")


Key = {
    '0':['HEAD','TRLR','NOTE'],
    '1':['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
    '2':"DATE"
}

IndiDict = {} #Key = Individual ID/ Data = individual class with that ID number
FamDict = {}
ParserErrors = []

class INDI:
    def __init__(self):
                self.id = '' #ID and Key in Dict
                self.name = '' 
                self.gender = '' #M/F
                self.dob = ''
                self.age = '' #NOT PROVIDED MUST CALCULATE
                self.alive = True
                self.death = 'N/A' #Date of Death
                self.child = 'N/A' #ID of Family they are a child in 
                self.spouse = [] #IDs of Families they are married into

class FAM:
    def __init__(self):
                self.id = ''
                self.married = 'N/A'
                self.divorce = 'N/A'
                self.husbandId = 'N/A'
                self.husbandName = 'N/A'
                self.wifeId = 'N/A'
                self.wifeName = 'N/A'
                self.children = []

def makeINDI(id,name,gender,dob,age,alive,death,child,spouse):
    indi = INDI()
    indi.id = id
    indi.name = name
    indi.gender = gender
    indi.dob = dob
    indi.age = age
    indi.alive = alive
    indi.death = death
    indi.child = child
    indi.spouse = spouse
    return indi

def makeFAM(id,married,divorce,husbandId,husbandName,wifeId,wifeName,children):
    fam = FAM()
    fam.name = id
    fam.married = married
    fam.divorce = divorce
    fam.husbandId = husbandId
    fam.husbandName = husbandName
    fam.wifeId = wifeId
    fam.wifeName = wifeName
    fam.children = children
    return fam

current = None
isIndi = None
dateType = None
for line in GEDCOM.readlines():
    words = line.split()
    if words[0] not in Key.keys(): #Not valid
        print('bad leading number')
        continue

    if words[1] in Key[words[0]]: #valid index keyword pair
        if current is None and words[0] != '0': #no indi/fam selected but info is added
            continue
        if words[0] == '0': #Skips for Head, TRLR, and 'Note' tags
            if isIndi is None:
                continue
            elif isIndi:
                IndiDict[current.id] = current
                current = None
                isIndi = None
            else:
                FamDict[current.id] = current
                current = None
                isIndi = None
        elif words[1] == 'NAME': #Checks if NAME tag is correctly applied to INDI
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                current.name = " ".join(words[2:])
            else:
                print('Invlaid FAM Value')
        elif words[1] == 'SEX':   #Checks if SEX tag is correctly applied to INDI
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                current.gender = " ".join(words[2:])
            else:
                print('Invalid FAM Value')
        elif words[1] == 'BIRT':  #Checks if BIRT tag is correctly applied to INDI, and Date Follows
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                dateType = 'BIRT'
            else:
                print('Invalid Fam Value')
        elif words[1] == 'DEAT':  #Checks if DEAT tag is correctly applied to INDI, and Date Follows
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                dateType = 'DEAT'
                current.alive = False       
            else:
                print('Invalid Fam Value')
        elif words[1] == 'MARR':  #Checks if MARR tag is correctly applied to FAM, and Date Follows
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                print('Invalid Indi Value')
            else:
                dateType = 'MARR'
        elif words[1] == 'DIV':  #Checks if DIV tag is correctly applied to FAM, and Date Follows
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                print('Invalid Indi Value')
            else:
                dateType = 'DIV'
        elif words[1] == 'DATE': #Cycles through all possible values of preceeding tags, then adds the info
            if dateType is None:
                print('Date Error')
            elif dateType == 'BIRT':
                current.dob = " ".join(words[2:])
                dateType = None
            elif dateType == 'DEAT':
                current.death = " ".join(words[2:])
                dateType = None
            elif dateType == 'MARR':
                current.married = " ".join(words[2:])
                dateType = None
            else:
                current.divorce = " ".join(words[2:])
                dateType = None
        elif words[1] == 'FAMC': #Adds ID of the Individual's Childhood Family
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                current.child = " ".join(words[2:])
            else:
                print('Invalid FAM Value')
        elif words[1] == 'FAMS': #Adds ID of Family Individual Has Married Into
            if isIndi is None:
                print('Invalid GEDCOM')
            elif isIndi:
                current.spouse.append(" ".join(words[2:]))
            else:
                print('Invalid FAM Value')
        elif words[1] == 'HUSB': #Adds the Name and ID of a Husband to a Family
            if isIndi is None: 
                print('Invalid GEDCOM')
            elif isIndi:
                print('Invalid INDI Value')
            else:
                current.husbandId = " ".join(words[2:])
                if current.husbandId in IndiDict.keys():
                    current.husbandName = IndiDict[current.husbandId].name
        elif words[1] == 'WIFE': #Adds the Name and ID of a Wife to a Family
            if isIndi is None: 
                print('Invalid GEDCOM')
            elif isIndi:
                print('Invalid INDI Value')
            else:
                current.wifeId = " ".join(words[2:])
                if current.wifeId in IndiDict.keys():
                    current.wifeName = IndiDict[current.wifeId].name
        elif words[1] == 'CHIL': #Adds the ID of the children to a Family
            if isIndi is None: 
                print('Invalid GEDCOM')
            elif isIndi:
                print('Invalid INDI Value')
            else:
                current.children.append(" ".join(words[2:]))
        continue

    elif words[0] == '0' and words[2] == 'INDI': #edge case for INDI
        if current is None:
            if not (words[1] in IndiDict):
                current = INDI()
                current.id = words[1]
                IndiDict[current.id] = current
                isIndi = True
            else:
                ParserErrors.append('US22 Error: Only 1 instance of Individual ' + words[1] + ' is allowed.')
                current = None
                isIndi = None
        elif isIndi:
            if not (words[1] in IndiDict):
                current = INDI()
                current.id = words[1]
                IndiDict[current.id] = current
                isIndi = True
            else:
                ParserErrors.append('US22 Error: Only 1 instance of Individual ' + words[1] + ' is allowed.')
                current = None
                isIndi = None
        else:
            print('INDI Check Error')
        continue
        
    elif words[0] == '0' and words[2] == 'FAM': #edge case for FAM
        if current is None:
            if not (words[1] in FamDict):
                current = FAM()
                current.id = words[1]
                FamDict[current.id] = current
                isIndi = False
            else:
                ParserErrors.append('US22 Error: Only 1 instance of Family ' + words[1] + ' is allowed.')
                current = None
                isIndi = None
        elif isIndi:
            if not (words[1] in FamDict):
                current = FAM()
                current.id = words[1]
                FamDict[current.id] = current
                isIndi = False
            else:
                ParserErrors.append('US22 Error: Only 1 instance of Family ' + words[1] + ' is allowed.')
                current = None
                isIndi = None
        else:
            if not (words[1] in FamDict):
                current = FAM()
                current.id = words[1]
                FamDict[current.id] = current
                isIndi = False
            else:
                ParserErrors.append('US22 Error: Only 1 instance of Family ' + words[1] + ' is allowed.')
                current = None
                isIndi = None
        continue

    else: #invalid index keyword pair
        #print('invalid index keyword pair')
        continue

GEDCOM.close()

def calculate_age(birthDate,currentDate):
    if ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day)):
        return currentDate.year - birthDate.year - 1
    else:
        return currentDate.year - birthDate.year

#Marriage before divorce
def US04(fam):
    if(FamDict[fam].married != 'N/A' and FamDict[fam].divorce != 'N/A'):
        mardate = datetime.strptime(FamDict[fam].married, '%d %b %Y')
        divdate = datetime.strptime(FamDict[fam].divorce, '%d %b %Y')
        if (divdate < mardate):
            return False  
    if(FamDict[fam].married == 'N/A' and FamDict[fam].divorce != 'N/A'):
            return False
    return True

#Divorce before death
def US06(fam):
    if((FamDict[fam].divorce != 'N/A') and (IndiDict[FamDict[fam].husbandId].alive != True) and (IndiDict[FamDict[fam].wifeId].alive != True)):
        divdate = datetime.strptime(FamDict[fam].divorce, '%d %b %Y')
        husbdeath = datetime.strptime(IndiDict[FamDict[fam].husbandId].death, '%d %b %Y')
        wifedeath = datetime.strptime(IndiDict[FamDict[fam].wifeId].death, '%d %b %Y')
        if (divdate > husbdeath) or (divdate > wifedeath):
            return False
        return True

for person in IndiDict:
    birthDate = datetime.strptime(IndiDict[person].dob, '%d %b %Y')
    if (IndiDict[person].alive == True):
        currentDate = date.today()
    else:
        currentDate = datetime.strptime(IndiDict[person].death, '%d %b %Y')
    IndiDict[person].age = calculate_age(birthDate,currentDate)

#Merge Test - Jayson