'''
Created on Dec 2, 2016

@author: maleone
'''

with open("data/day03") as f:
    print "Part 1"
    count = 0;
    for line in f:
        t = line.split()
        if not (int(t[0]) >= int(t[1]) + int(t[2]) or \
                int(t[1]) >=int(t[0]) + int(t[2]) or \
                int(t[2]) >= int(t[0]) + int(t[1])):
                    count+=1
    print count
    
with open("data/day03") as f:
    print "Part 2"
    count = 0;
    trans = [x.split() for x in f]
    for z in zip(*trans):
        for t in zip(*[iter(z)]*3):
            if not (int(t[0]) >= int(t[1]) + int(t[2]) or \
                    int(t[1]) >=int(t[0]) + int(t[2]) or \
                    int(t[2]) >= int(t[0]) + int(t[1])):
                        count+=1
    print count