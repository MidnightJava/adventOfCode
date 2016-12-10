'''
Created on Dec 9, 2016

@author: maleone
'''

import re, time

with open("data/day09", "r") as f:
    expanded = ""
    data=f.read().replace('\n', '')
    data = " ".join(data.split())
    index = 0
    while index < (len(data)-1):
#         print "Expanded len", len(expanded)
        if data[index] == "(":
            m = re.search("\(([^)]+)\)", data[index:])
            if m:
                s = m.group(1).split("x")
                ccount = int(s[0])
                reps = int(s[1])
                index+= (len(m.group(1)) + 2)
                toAdd = data[index:index+ccount]
                for x in xrange(reps):
                    expanded+= toAdd
                index+= ccount
            else:
                expanded+= data[index]
                index+= 1
        else:
            expanded+= data[index]
            index+= 1
    print len(expanded)
    
def decompress(m, data, index):
    count = 0
    added = ""
    startTime = time.time()
    while m and time.time() - startTime < 30:
        s = m.group(1).split("x")
        ccount = int(s[0])
        reps = int(s[1])
        count+= (len(m.group(1)) + 2)
        toAdd = data[index:index+ccount]
        for x in xrange(reps):
            added+= toAdd
        count+= ccount
        index = len(m.group(1))
#         m = re.search("\(([^)]+)\)", data[index:])
        m = None
    return added, count

#Part 2
with open("data/day09", "r") as f:
    expandedCount = 0
    data=f.read().replace('\n', '')
    data = " ".join(data.split())
    index = 0
    while index < (len(data)-1):
    #         print "Expanded len", len(expanded)
        if data[index] == "(":
            m = re.search("\(([^)]+)\)", data[index:])
            index2 = index
            if m:
                start = time.time()
                while m:# and time.time() - start < 60:
                    added,count = decompress(m, data, index2)
                    expandedCount+= len(added)
                    index+= count
                    index2 = 0
                    m = re.search("\(([^)]+)\)", added)
        else:
            expandedCount+= 1
            index+= 1
    print expandedCount
