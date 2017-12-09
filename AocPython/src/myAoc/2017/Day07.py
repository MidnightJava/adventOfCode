'''
Created on Dec 6, 2017

@author: Mark
'''

import re
from __builtin__ import int
from collections import defaultdict

class program:
    def __init__(self, name, weight, plst):
        self.name = name
        self.weight = weight
        self.plst = plst

    def __str__(self):
        if self.plst:
            return self.name + " " + self.weight + " " + ",".join(self.plst)
        else:
            return self.name + " " + self.weight


programs = {}
stacked = []

with open("data/Day07") as f:
    for line in f:
        m = re.search("^(\w+)\s+\((\d+)\)\s*(.*)?$", line.strip())
        name = m.group(1)
        weight = m.group(2)
        if m.group(3).strip() == '':
            plst = None
        else:
            g3 = m.group(3)
            plst = re.search("\-\>\s+(.*)$", m.group(3).strip()).group().replace("->", "").strip().split(",")
            for p in plst:
                stacked.append(p.strip())
        prog = program(name, int(weight), plst)
        programs[prog.name] = prog


for item in programs.items():
    if not item[0] in stacked:
        rootProg = item[1]
        break
def getWeight(prog):
    weight = prog.weight
    if prog.plst:
        for p in prog.plst:
            weight+= getWeight(programs[p.strip()])
    return weight


def getCorrectedWeight(prog, diff):
    #Look at total weights of all immediate towers.
    # If same, then return prog.weight + diff
    # If different, recurse with prog that has unique weight and current diff
    # Will not encounter case where only 2 towers and they're different

    d = defaultdict(list)
    for p in prog.plst:
        w = getWeight(programs[p.strip()])
        d[w].append(programs[p.strip()])
    if len(d.items()) == 1:
        #All children have same weight
        return prog.weight + diff
    for item in d.items():
        if len(item[1]) == 1 and item[1][0].plst != None:
            #This is the different one
            w1 = item[0]
            for item2 in d.items():
                if item2[0] != w1:
                    newDiff = item2[0] - w1
                    break
            return getCorrectedWeight(item[1][0], newDiff)

    print "Didn't find unique weight", prog

print "Part 1", rootProg.name
print "Part 2", getCorrectedWeight(rootProg, 0)

