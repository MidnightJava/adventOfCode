'''
Created on Dec 20, 2016

@author: maleone
'''

# Naive implementation to analyze the problem behavior. Keep a list of index ranges
# representing removed elves, but even with this optimization it seems like it would
# take a month or so to get a solution.

numelfs = 3004953
numelfs = 21
remaining = numelfs
gone = []

def makeGone(elf):
    global gone, remaining
    mergeGoneElf(elf)
    remaining-= 1
def isGone(elf):
    global ig
    for r in gone:
        if r[0] <= elf <= r[1]:
            return True
    return False

def mergeGoneElf(elf):
    global gone
    for r in gone:
        if r[0] <= elf < r[1]:
            return
        elif r[1] == elf - 1:
            index = gone.index(r)
            r = (r[0],elf)
            gone[index] = r
            return
        elif r[0] == elf + 1:
            index = gone.index(r)
            r = (elf, r[1])
            gone[index] = r
            return
    gone.append((elf,elf))
    gone = sorted(gone, key=lambda tup: tup[0])

def nextElf(i):
    goner = (i + 1) % numelfs
    elf_gone = isGone(goner)
    while elf_gone:
        goner = (goner + 1) % numelfs
        goner = numelfs if goner == 0 else goner
        elf_gone = isGone(goner)
    makeGone(goner)
    next_elf = (goner + 1) % numelfs
    next_elf = numelfs if next_elf == 0 else next_elf
    next_elf_found = not isGone(next_elf)
    while not next_elf_found:
        next_elf = (next_elf + 1) % numelfs
        next_elf = numelfs if next_elf == 0 else next_elf
        next_elf_found = not isGone(next_elf)
    return numelfs if next_elf == 0 else next_elf

def solve(elf):
    while remaining > 1:
        elf = nextElf(elf)
        if remaining % 10000 == 0:
            print "remaining", remaining
    print "last elf:", elf
    
solve(1)