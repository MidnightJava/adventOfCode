'''
Created on Dec 8, 2017

@author: Mark
'''

from collections import defaultdict 

regs = defaultdict(int)

hi2 = 0

with open("data/Day08") as f:
    for line in f:
        reg1, op, val1, _if, reg2, cond, val2 = line.split()
        if cond == '<':
            if regs[reg2] < int(val2):
                regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        elif cond == '>':
            if regs[reg2] > int(val2):
               regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        elif cond == '<=':
            if regs[reg2] <= int(val2):
                regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        elif cond == '>=':
            if regs[reg2] >= int(val2):
                regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        elif cond == '==':
            if regs[reg2] == int(val2):
                regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        elif cond == '!=':
            if regs[reg2] != int(val2):
                regs[reg1] = regs[reg1] - int(val1) if op == 'dec' else regs[reg1] + int(val1)
        else:
            print "unknown condition", cond
        if regs[reg1] > hi2:
            hi2 = regs[reg1]
                
hi = 0

for item in regs.items():
    if item[1] > hi:
        hi = item[1]
print "Part 1", hi
print "Part 2", hi2
