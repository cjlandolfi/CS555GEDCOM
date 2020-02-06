FamilyTree = open("proj02test.ged", "r")
Key = {
    '0':['HEAD','TRLR','NOTE'],
    '1':['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
    '2':"DATE"
}

for line in FamilyTree.readlines():
    print("--> " + line.rstrip())
    words = line.split()
    if words[0] not in Key.keys():
        print(f'<--{words[0]}|{words[1]}|N|{" ".join(words[2:])}')
        continue
    if words[1] in Key[words[0]]: #valid index keyword pair
        print(f'<--{words[0]}|{words[1]}|Y|{" ".join(words[2:])}')
        continue
    elif words[0] == '0' and (words[2] == 'INDI' or words[2] == 'FAM'): #edge case for INDI and FAM
        print(f'<--{words[0]}|{words[2]}|Y|{words[1]}')
        continue
    else: #invalid index keyword pair
        print(f'<--{words[0]}|{words[1]}|N|{" ".join(words[2:])}')
        continue
    
FamilyTree.close()