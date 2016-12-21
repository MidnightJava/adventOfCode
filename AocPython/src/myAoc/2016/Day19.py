'''
Created on Dec 19, 2016

@author: Mark
'''

numelfs = 3004953
elfs = numelfs

class NextElf:
    def __init__(self, elf):
        self.elf = elf
    
    def setElf(self, elf):
        self.elf = elf
        return self.elf
    
    def getNextElfFunc(self, l):
        def f(n):
            self.elf = (self.elf + n) % l
            self.elf = l if self.elf == 0 else self.elf
            return self.elf
        return f

ne = NextElf(numelfs)
f = ne.getNextElfFunc(numelfs)
n = 2
nextElf = None
cd = divmod(numelfs, 2)
ncount = cd[0]
while elfs > 1:
    for i in xrange(0, numelfs+n, n):
        if numelfs -i + 1 <= n:
            ncount-= 1
            continue
        elif i < n and n > 2:
            nextElf = ne.setElf(n/2 - 1)
#             print "next elf", nextElf
            ncount-= 1
            elfs-= 1
            continue
        nextElf = f(n)
#         print "next elf", nextElf
        elfs-= 1
        ncount-= 1
        if ncount == 0:
            n*= 2
            print "n=",n
            cd = divmod(elfs, 2)
            ncount = cd[0]

print "elfs left", elfs
print "last elf", f(n/2)

