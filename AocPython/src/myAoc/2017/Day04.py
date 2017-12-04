'''
Created on Dec 4, 2017

@author: maleone
'''
from collections import defaultdict

count = 0
with open("data/Day04") as f:
    for line in f:
        if len(line.split()) == len(set(line.split())):
            count+= 1
    print "Part 1:", count

count = 0
with open("data/Day04") as f:
    for line in f:
        if len(line.split()) != len(set(line.split())):
            continue
        valid = True
        words = line.split()
        for w in words:
            w_freq = defaultdict(int)
            for c in w.strip():
                w_freq[c]+= 1
            for w2 in words:
                if w == w2:
                    continue
                w2_freq = defaultdict(int)
                for c in w2.strip():
                    w2_freq[c]+= 1
                if cmp(w_freq, w2_freq) == 0:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count+= 1

    print "Part 2:", count

