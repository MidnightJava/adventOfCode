'''
Created on Dec 16, 2016

@author: Mark
'''

from itertools import izip

size =[272, 35651584]

def scramble(a, s):
    while len(a) < s:
        b = a[::-1]
        a = a + "0" + ''.join('1' if x == '0' else '0' for x in b)
    return a[:s]

def checksum(s):
    chksum = None
    done = False
    while not done:
        chksum = ""
        ab = iter(s)
        for a,b in izip(ab, ab):
            if a == b:
                chksum += "1"
            else:
                chksum += "0"
        if len(chksum) % 2 == 0:
            s = chksum
            chksum = ""
        else:
            done = True
    return chksum
            
data = "10111100110001111"
for s in size:
    d = scramble(data, s)
    print checksum(d)