'''
Created on Dec 4, 2016

@author: Mark
'''
from collections import Counter
import collections
import re

def p(lst):
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

def decr(name, shft):
    decrn = ""
    for c in name:
        intval = ord(c) - ord("a")
        shifted = (intval + shft) % 26
        sc = chr(shifted + ord("a"))
        decrn+= sc
        
    if "north" in decrn:
        print "North Pole Sector:", shft
        

#list sorted by frequencies
# lst =sorted("gggxxxxaakymz")
# counts = Counter(lst)
# new_list = sorted(lst, key=lambda x: -counts[x])
# #new_list = sorted(lst, key=counts.get, reverse=True)
# new_list = p(new_list)
# print new_list

with open("data/day04") as f:
    count = 0
    for line in f:
        m = re.search("([\w|\-]+)\-(\d+)\[(\w{5})\]", line.strip())
        name = m.group(1).strip().replace("-", "")
        sn = sorted(name)
        sector = int(m.group(2))
        decr(name, sector)
        chksum = m.group(3)
        
        counts = Counter(sn)
        new_list = p(sorted(sn, key=lambda x: -counts[x]))
        if (len(chksum) == 5 and collections.Counter(new_list[0:5]) == collections.Counter(list(chksum))):
            count+= sector
        
    print "Total: ", count

        