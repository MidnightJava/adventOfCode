'''
Created on Dec 6, 2016

@author: Mark
'''

import re
def abba(s):
    for x in range(len(s) - 3):
        if s[x] == s[x+3] and s[x+1] == s[x+2]:
            return True
    return False

def aba(s1, s2):
    inbrackets = False
    lookfor = s2[1] + s2[0] + s2[1]
    for x in range(len(s1) - 2):
        if s1[x] == '[':
            inbrackets = True
        elif s1[x] == ']':
                inbrackets = False
        elif not inbrackets:
            if s1[x:x+3] == lookfor:
                return True
    return False

def bab(s):
    babs = []
    for x in range(len(s) - 2):
        if s[x] != s[x+1] and s[x] == s[x+2]:
            babs.append(s[x:x+3])
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
        m = re.findall("\[[^\[\]]+\]", line.strip())
        if m:
            done = False
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