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
    
with open("data/day07") as f:
    count = 0
    for line in f:
        m = re.findall("\[.*\]", line.strip())
        if m and len(m) > 0:
            done = False
            for g in m:
                if not done and abba(g[1:len(g)-1]):
                    if abba(line.strip()):
                        count+= 1
                        done = True
                        break
        elif abba(line.strip()):
                count+= 1
                        
    print count
