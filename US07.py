from Parser import FamDict,IndiDict

def US07(person):
    if IndiDict[person].age > 150:
        return True
    else:
        return False