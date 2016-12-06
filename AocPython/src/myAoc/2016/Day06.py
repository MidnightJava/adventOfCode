'''
Created on Dec 6, 2016

@author: maleone
'''

from collections import Counter

with open("data/day06") as f:
    p1 = p2 = ""
    trans = [list(x) for x in f]
    for z in zip(*trans):
        counts = Counter(sorted(z))
        p1 += sorted(z, key=lambda x: -counts[x])[0]
        p2 += sorted(z, key=lambda x: counts[x])[0]
    print "Part 1", p1
    print "Part 2", p2
        
        