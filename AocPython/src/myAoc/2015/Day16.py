'''
Created on Dec 16, 2015

@author: maleone
'''
import re

regex = "^Sue\s(\d+)\:(?:\s(\w+)\:\s(\d+)\,?)(?:\s(\w+)\:\s(\d+)\,?)(?:\s(\w+)\:\s(\d+)\,?)$"
stext = "children:3:cats:7:samoyeds:2:pomeranians:3:akitas:0:vizslas:0:goldfish:5:trees:3:cars:2:perfumes:1:"
with open("auntsues.txt" ) as f:
    for line in f:
        sueNum, w1, n1, w2, n2, w3, n3 = re.findall(regex, line)[0]
        found = True
        for s in [ w1 + "\\:" + n1 + "\:",  w2 + "\\:" + n2 + "\\:",  w3 + "\\:" + n3 + "\\:"]:
            if not re.search(s, stext):
                found = False
        if found:
            print "Aunt Sue number ", sueNum
            break
#Part 2
stextP2 = "children:3:samoyeds:2:akitas:0:vizslas:0:cars:2:perfumes:1:"       
with open("auntsues.txt" ) as f:
    for line in f:
        sueNum, w1, n1, w2, n2, w3, n3 = re.findall(regex, line)[0]
        found = True
        sList = []
        if w1 != 'cats' and w1 != 'trees' and w1 != 'pomeranians' and w1 != 'goldfish':
            sList.append(w1 + "\\:" + n1 + "\\:")
        if w2 != 'cats' and w2 != 'trees' and w2 != 'pomeranians' and w2 != 'goldfish':
            sList.append(w2 + "\\:" + n2 + "\\:")
        if w3 != 'cats' and w3 != 'trees' and w3 != 'pomeranians' and w3 != 'goldfish':
            sList.append(w3 + "\\:" + n3 + "\\:")
        for s in sList:
            if s and not re.search(s, stext):
                found = False
        if found:
            catNum = n1 if w1 == 'cats' else n2 if w2 == 'cats' else n3 if w3 == 'cats' else None
            treeNum = n1 if w1 == 'trees' else n2 if w2 == 'trees' else n3 if w3 == 'trees' else None
            pomNum = n1 if w1 == 'pomeranians' else n2 if w2 == 'pomeranians' else n3 if w3 == 'pomeranians' else None
            gfNum = n1 if w1 == 'goldfish' else n2 if w2 == 'goldfish' else n3 if w3 == 'goldfish' else None
            if (catNum and int(catNum) <= 7) or (treeNum and int(treeNum) <= 3) or (pomNum and int(pomNum) >= 3) or (gfNum and int(gfNum) >= 5):
                continue
            print "The REAL Aunt Sue number ", sueNum
            break