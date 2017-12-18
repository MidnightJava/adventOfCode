'''
Created on Dec 18, 2017

@author: maleone
'''
from _collections import defaultdict


d = defaultdict(int)
code = []
idx = 0

code = map(lambda x: x.strip(), open("data/Day18").readlines())
while idx >= 0 and idx < len(code):
    instr = code[idx]
    if "snd" in instr:
        val = instr.split()[1]
        play = d[val]
    elif 'set' in instr:
        parts = instr.split()
        reg, val = parts[1], parts[2]
        try:
            d[reg] = int(val)
        except ValueError:
            d[reg] = d[val]
    elif 'add' in instr:
        parts = instr.split()
        reg, val = parts[1], parts[2]
        try:
            d[reg]+= int(val)
        except ValueError:
            d[reg]+= d[val]
    elif 'mul' in instr:
        parts = instr.split()
        reg, val = parts[1], parts[2]
        try:
            d[reg]*= int(val)
        except ValueError:
            d[reg]*= d[val]
    elif 'mod' in instr:
        parts = instr.split()
        reg, val = parts[1], parts[2]
        try:
            d[reg]= d[reg] % int(val)
        except ValueError:
            d[reg]= d[reg] % d[val]
    elif 'rcv' in instr:
        parts = instr.split()
        val = parts[1]
        if val:
            print "Part 1:", play
            break
    elif 'jgz' in instr:
        parts = instr.split()
        val = parts[1]
        offset = parts[2]
        if d[val]:
            try:
                idx = idx + int(offset)
            except ValueError:
                idx = idx + d[offset]
            continue
    idx+= 1
print idx
