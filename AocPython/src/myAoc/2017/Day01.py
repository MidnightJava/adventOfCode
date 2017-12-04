'''
Created on Dec 1, 2017

@author: Mark
'''
with open("data/Day01") as f:
    n = 0
    for line in f:
        for i in xrange(len(line)):
            if i == len(line) - 1:
                nxt = 0
            else:
                nxt = (i+1)
            if line[i] == line[nxt]:
                n+= int(line[i])
    print "part 1", n
    
    n=0
with open("data/Day01") as f:
    for line in f:
        for i in xrange(len(line)):
            nxt = (i + (len(line) /2)) % len(line)
            if line[i] == line[nxt]:
                n+= int(line[i])
    print "part 2", n