'''
Created on Dec 24, 2015

@author: Mark
'''
from collections import namedtuple
a = 1
b = 0
prog = []
with open("registerops") as f:
    prog = [line.strip().strip(",").split() for line in f.readlines()]
#     print prog
    
index = 0
while index >= 0 and index < len(prog):
    print prog[index]
    prog[index][1] = prog[index][1].strip(",")
    if len(prog[index]) == 2:
        if prog[index][0] == 'jmp':
            index += int(prog[index][1])
        else:
            if prog[index][0] == 'hlf':
                if prog[index][1] == 'a':
                    a /= 2
                else:
                    b /= 2
            elif prog[index][0] == 'tpl':
                if prog[index][1] == 'a':
                    a *= 3
                else:
                    b *= 3
            else:
                if prog[index][1] == 'a':
                    a += 1
                else:
                    b += 1
            index += 1
    else:
        regval = a if prog[index][1] == 'a' else b
        if prog[index][0] == 'jie':
            if regval % 2 == 0:
                index += int(prog[index][2])
            else:
                index += 1
        else:
            if regval == 1:
                index += int(prog[index][2])
            else:
                index += 1
    print a, b
                
print b
    
        