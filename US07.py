import Parser as Parser
from Parser import IndiDict

for person in IndiDict:
    if IndiDict[person].age > 150:
        print("US07 Error for " + IndiDict[person].name)