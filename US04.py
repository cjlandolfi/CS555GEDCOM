import Parser as Parser
from Parser import FamDict,IndiDict
from datetime import datetime, date

#US04: Marriage should occur before divorce of spouses, and divorce can only occur after marriage
for family in FamDict:
    if (FamDict[family].married != 'N/A' and FamDict[family].divorce != 'N/A'):
        mardate = datetime.strptime(FamDict[family].married, '%d %b %Y')
        divdate = datetime.strptime(FamDict[family].divorce, '%d %b %Y')
        if (divdate < mardate):
            print("US04 Error for Family: " + str(FamDict[family].id))
    if (FamDict[family].married == 'N/A' and FamDict[family].divorce != 'N/A'):
            print("US04 Error for Family: " + str(FamDict[family].id))


#ALTERNATE VERSION
# def US04(fam):
#     if(FamDict[fam].married != 'N/A' and FamDict[fam].divorce != 'N/A'):
#         mardate = datetime.strptime(FamDict[fam].married, '%d %b %Y')
#         divdate = datetime.strptime(FamDict[fam].divorce, '%d %b %Y')
#         if (divdate < mardate):
#             return False  
#     if(FamDict[fam].married == 'N/A' and FamDict[fam].divorce != 'N/A'):
#             return False
#     return True

#Running the alternate version through the entire file
# for fam in FamDict:
#     if(US04(fam)==False):
#         print("US04 Error for Family: " + str(FamDict[family].id))

#UNIT TEST THAT TESTS THE US04 METHOD, how do I instantiate a simple example of a family?
# class TestUserStories(unittest.TestCase):
#     def test_US04(self):
#         self.assertEqual(US04(),True)