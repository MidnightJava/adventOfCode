'''
Created on Dec 6, 2017

@author: Mark
'''

def highest(banks):
    hi = 0
    idx = 16
    for x in xrange(len(banks)):
        if banks[x] > hi:
            hi = banks[x]
            idx = x
        elif banks[x] == hi:
            if x < idx:
                idx = x
                
    return idx, hi

f = open("data/Day06")

for line in f:
    banks = map(lambda x: int(x), line.split())

seen = []

count = 0
count2 = 0
found = False
target = None
while True:
    if found and banks == target:
        print "Part 2", count2
        break
    if not found and banks in seen:
        print "Part 1", count
        found = True
        target = banks[:]
        count2 = 0
    seen.append(banks[:])
    idx, val = highest(banks)
    nxt = idx
    for i in xrange(val):
        nxt = (nxt + 1) % 16
        banks[nxt]+= 1
        banks[idx]-= 1
    count+= 1
    count2+= 1
        