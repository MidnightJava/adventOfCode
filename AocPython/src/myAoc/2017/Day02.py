'''
Created on Dec 2, 2017

@author: Mark
'''

with open("data/Day02") as f:
    diffs = []
    for row in f:
        low = 1e12
        high = 0
        for num in row.split():
            if int(num) < low:
                low = int(num)
            if int(num) > high:
                high = int(num)
        diffs.append(high - low)
    print "Part 1", sum(diffs)
    
with open("data/Day02") as f:
    divs = []
    for row in f:
        done = False
        for i in xrange(len(row.split())):
            if done:
                done = False
                break
            for j in xrange(i+1, len(row.split())):
                a = int(row.split()[i])
                b = int(row.split()[j])
                if a % b == 0 or b % a == 0:
                    divs.append(max(a,b) / min(a,b))
                    done = True
                    break;
    print "Part 2", sum(divs)