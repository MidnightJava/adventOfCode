'''
Created on Dec 19, 2016

@author: Mark
'''

import bisect

numelfs = 3004953
numelfs = 21
elfs = numelfs
a = [1]*numelfs

def nextElf(elf):
    nextelf = (elf + 1) % numelfs
    while nextelf in gone:
        nextelf = (bisect.bisect(gone, nextelf) + 1) % numelfs
    return numelfs if nextelf == 0 else nextelf

def steal(elf):
    global gone
    bisect.insort(gone, elf)
    return nextElf(elf)

# elf = 1
# while len(gone) < numelfs -1:
#     elf = steal((elf + 1) % numelfs)
# print elf -2

class NextElf:
    def __init__(self, x):
        self.x = x
    
    def setX(self, x):
        self.x = x
        self.lastX = x
        return self.x
    
    def ungetLastElf(self):
        self.x = self.lastX
    
    def getnextf(self, l):
        def f(n, x):
            if x:
                self.x = x
            self.lastX = self.x
            self.x = (self.x + n) % l
            self.x = l if self.x == 0 else self.x
            return self.x
        return f

ne = NextElf(numelfs)
f = ne.getnextf(numelfs)
n = 2
lastelf = None
while elfs >= 1 and n <= numelfs:
    for i in xrange(0, numelfs-1, n):
        lastelf = elf = f(n, None)
        print "next elf", elf
        elfs-= 1
        a[lastelf-1] = 0
    if lastelf < n:
        ne.ungetLastElf()
        print "unget elf", lastelf
        elfs+= 1
    if lastelf % 2 == 0:
        lastelf = elf = ne.setX(n-1)
        print "*next* elf", lastelf
    else:
        lastelf = elf = ne.setX(2*n-1)
        print "*next* elf", lastelf
    elfs-= 1
    a[lastelf-1] = 0
    n*= 2
    print "n=",n
#     lastelf = n-1

print "elfs left", elfs
print "LAST ELF", lastelf, f(n, None)
print a

