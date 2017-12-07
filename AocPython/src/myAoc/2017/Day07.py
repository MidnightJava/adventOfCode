'''
Created on Dec 6, 2017

@author: Mark
'''

import re

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
        
        
programs = []

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
        programs.append(program(name, weight, plst))
        
    for i in xrange(len(programs)):
            print programs[i]
        