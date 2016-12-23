'''
Created on Dec 23, 2016

@author: maleone
'''
import re

def toggle(n):
    if n >= len(prog):
        return
    if prog[n].startswith("inc"):
        prog[n] = prog[n].replace("inc", "dec")
    elif prog[n].startswith("dec"):
        prog[n] = prog[n].replace("dec", "inc")
    elif prog[n].startswith("tgl"):
        prog[n] = prog[n].replace("tgl", "inc")
    elif prog[n].startswith("jnz"):
        prog[n] = prog[n].replace("jnz", "cpy")
    elif prog[n].startswith("cpy"):
        prog[n] = prog[n].replace("cpy", "jnz")

def readProg():
    global prog
    with open("data/day23b") as f:
        prog = [line.strip() for line in f.readlines()]
    
for i in [True, False]:
    global regs
    readProg()
    index = 0
    count = 0
    part1 = i
    if i:
        regs = {"a":7, "b":0, "c":0, "d":0}
    else:
        regs = {"a":12, "b":0, "c":0, "d":0}
    while index >= 0 and index < len(prog):
    #     print prog[index]
        if count % 1000000 == 0:
            print regs
#         print "index", index
        incr = 1
        count+=1
        m = re.search("cpy (\D) (\w)", prog[index])
        if m:
            regs[m.group(2)] = regs[m.group(1)]
        else:
            m = re.search("cpy ([-]?\d+) (\w)", prog[index])
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
                            m = re.search("jnz (\d) (\D+)", prog[index])
                            if m:
                                if m.group(1) != 0:
                                    incr = regs[m.group(2)]
                            else:
                                m = re.search("jnz (\D) (-?)(\d+)", prog[index])
                                if m:
                                    if regs[m.group(1)] != 0:
                                        incr = int(m.group(3))
                                        incr = -incr if m.group(2) == "-" else incr
                                else:
                                    m = re.search("tgl (\D+)", prog[index])
                                    if m:
                                        toggle(index + regs[m.group(1)])
                                    else:
                                        m = re.search("mlt (\w) (\w)", prog[index])
                                        if m:
                                            regs[m.group(1)]+= abs(regs[m.group(2)])
                                        else:
                                            if not prog[index].startswith("nop"):
                                                print "bad instruction", prog[index]
        index+= incr
    
                
    print regs["a"]
