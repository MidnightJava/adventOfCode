'''
Created on Dec 9, 2016

@author: maleone
'''

import re, copy

#Part 1
with open("data/day09", "r") as f:
    expanded = ""
    data=f.read().replace('\n', '')
    data = "".join(data.split())
    index = 0
    while index < (len(data) - 1):
        if data[index] == "(":
            m = re.search("\((\d+)[xX](\d+)\)", data[index:])
            ccount = int(m.group(1))
            reps = int(m.group(2))
            index+= len(m.group(0))
            toAdd = data[index:index + ccount]
            expanded+= toAdd*reps
            index+= ccount
        else:
            expanded+= data[index]
            index+= 1
    print "Part 1:", len(expanded)

#Recursive approach. Probably correct, but will take forever
def expand2(data):
    index = 0
    count = 0
    while index < len(data):
        if data[index] == "(":
            m = re.search("\((\d+)[Xx](\d+)\)", data[index:])
            if m:
                ccount = int(m.group(1))
                reps = int(m.group(2))
                index+= len(m.group(0))
                toAdd = copy.deepcopy(data[index:index+ccount])
                index+= ccount
                count+= expand2(toAdd*reps)
        else:
            count+= 1
            index+= 1
    return count

def getStackMult(stck, index):
    mult = 1
    for t in stck:
        f,l,i = t[0], t[1], t[2]
        if index - i < l:
            mult*= f
    return mult
    
def expand(data):
    index = 0
    count = 0
    stck = []
    while index < len(data):
#         print "index: ", index
        if data[index] == "(":
            m = re.search("\((\d+)[Xx](\d+)\)", data[index:])
            if m:
                ccount = int(m.group(1))
                reps = int(m.group(2))
                index+= len(m.group(0))
                stck.append((reps, ccount, index))
        else:
            count+= getStackMult(stck, index)
            index+= 1
    return count

#Part 2
with open("data/day09", "r") as f:
    data=f.read().replace('\n', '')
    data = "".join(data.split())
    print "Part 2:", expand(data)