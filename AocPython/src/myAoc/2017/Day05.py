'''
Created on Dec 5, 2017

@author: Mark
'''

stack = {}

with open("data/Day05") as f:
    lines = []
    for line in f:
        lines.append(line.strip())
    for x in xrange(1, len(lines) + 1):
        stack[x] = int(lines[x-1])
    
    idx = 1
    count = 0
    while True:
        count+=1
        jmp = stack[idx]
        if jmp >= 3:
            stack[idx]-= 1
        else:
            stack[idx]+=1
        idx+= jmp
        if idx > len(stack):
            print count
            break
        