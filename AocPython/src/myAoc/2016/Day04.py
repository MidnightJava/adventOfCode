'''
Created on Dec 4, 2016

@author: Mark
'''
from collections import Counter
import re

def sortyByFreqThenAlpha(lst):
    new_lst = []
    last = None
    for x in xrange(0, len(lst) - 1):
        if  lst[x] != last:
            if lst[x] != lst[x+1]:
                new_lst.extend(sorted(lst[x:]))
                break
            else:
                new_lst.append(lst[x])
                last = lst[x]
    return new_lst

def decrypt(name, shft):
    decrName = ""
    for c in name:
        val = ord(c) - ord("a")
        shifted = (val + shft) % 26
        shiftedChar = chr(shifted + ord("a"))
        decrName+= shiftedChar
        
    if "northpoleobjectstorage" in decrName:
        print "North Pole Sector:", shft

with open("data/day04") as f:
    idSum = 0
    for line in f:
        m = re.search("([\w|\-]+)\-(\d+)\[(\w{5})\]", line.strip())
        if m:
            name = m.group(1).strip().replace("-", "")
            sector = int(m.group(2))
            decrypt(name, sector)
            chkSum = list(m.group(3))
            
            counts = Counter(sorted(name))
            sortedList = sortyByFreqThenAlpha(sorted(sorted(name), key=lambda x: -counts[x]))
            if sortedList[0:5] == chkSum:
                idSum+= sector
        
    print "Sum of IDs: ", idSum

        