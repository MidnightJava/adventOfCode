'''
Created on Dec 13, 2016

@author: Mark
'''
import re
regs = {"a":0, "b":0, "c":1, "d":0}
prog = []
with open("data/day12") as f:
    prog = [line.strip() for line in f.readlines()]
#     print prog
    
index = 0
count = 0
while index >= 0 and index < len(prog):
#     print prog[index]
    if count % 100000 == 0:
        print regs
    incr = 1
    count+=1
    m = re.search("cpy (\D) (\w)", prog[index])
    if m:
        regs[m.group(2)] = regs[m.group(1)]
    else:
        m = re.search("cpy (\d+) (\w)", prog[index])
        if m:
            regs[m.group(2)] = int(m.group(1))
        else:
            m = re.search("inc (\w)", prog[index])
            if m:
                regs[m.group(1)]+=1
            else:
                m = re.search("dec (\w)", prog[index])
                if m:
                    regs[m.group(1)]-=1
                else:
                    m = re.search("jnz (\d) (-?)(\d+)", prog[index])
                    if m:
                        if m.group(1) != 0:
                            incr = int(m.group(3))
                            incr = -incr if m.group(2) == "-" else incr
                    else:
                        m = re.search("jnz (\D) (-?)(\d+)", prog[index])
                        if m:
                            if regs[m.group(1)] != 0:
                                incr = int(m.group(3))
                                incr = -incr if m.group(2) == "-" else incr
    index+= incr
    
                
print regs["a"]