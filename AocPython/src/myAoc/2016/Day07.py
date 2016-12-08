'''
Created on Dec 6, 2016

@author: Mark
'''

import re
def abba(line):
    for x in range(len(line) - 3):
        if line[x] == line[x+3] and line[x+1] == line[x+2]:
            return True
    return False

def aba(line, pattern):
    inbrackets = False
    lookfor = pattern[1] + pattern[0] + pattern[1]
    for x in range(len(line) - 2):
        if line[x] == '[':
            inbrackets = True
        elif line[x] == ']':
                inbrackets = False
        elif not inbrackets:
            if line[x:x+3] == lookfor:
                return True
    return False

def bab(line):
    babs = []
    for x in range(len(line) - 2):
        if line[x] != line[x+1] and line[x] == line[x+2]:
            babs.append(line[x:x+3])
    return babs
   
#Part 1 
with open("data/day07") as f:
    count = 0
    for line in f:
        m = re.findall("\[.*\]", line.strip())
        if m:
            done = False
            for g in m:
                if not done and abba(g[1:len(g)-1]):
                    if abba(line.strip()):
                        count+= 1
                        done = True
                        break
        elif abba(line.strip()):
            count+= 1
                        
    print "Part 1:", count

#Part 2 
with open("data/day07") as f:
    count = 0
    for line in f:
        done = False
        m = re.findall("\[[^\[\]]+\]", line.strip())
        if m:
            for g in m:
                if not done:
                    babs = bab(g[1:len(g)-1])
                    for s_bab in babs:
                        if not done:
                            if aba(line, s_bab):
                                count+= 1
                                done = True
                                break
    print "Part 2:", count