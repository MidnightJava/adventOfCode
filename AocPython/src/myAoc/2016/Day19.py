'''
Created on Dec 19, 2016

@author: Mark
'''

import bisect

numelfs = 3004953
# numelfs = 5
gone = []

def nextElf(elf):
    nextelf = (elf + 1) % numelfs
    while nextelf in gone:
        nextelf = (bisect.bisect(gone, nextelf) + 1) % numelfs
    return numelfs if nextelf == 0 else nextelf

def steal(elf):
    global gone
    bisect.insort(gone, elf)
    return nextElf(elf)

elf = 1
while len(gone) < numelfs -1:
    elf = steal((elf + 1) % numelfs)
print elf -2