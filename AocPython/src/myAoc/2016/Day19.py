'''
Created on Dec 19, 2016

@author: Mark
'''

numelfs = 3004953
numelfs = 15
elfs = numelfs

class NextElf:
    def __init__(self, x):
        self.x = x
    
    def setX(self, x):
        self.x = x
        self.lastX = x
        return self.x
    
    def ungetLastElf(self):
        oldx = self.x
        self.x = self.lastX
        return oldx
    
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
cd = divmod(numelfs, 2)
ncount = cd[0]
while elfs > 1 and n < numelfs:
    for i in xrange(0, numelfs, n):
        if numelfs - i + 1 < n:
            print "unget elf", ne.ungetLastElf()
            continue
        lastelf = elf = f(n, None)
        print "next elf", elf
        elfs-= 1
        ncount-= 1
        if ncount == 0:
            n*= 2
            print "n=",n
            cd = divmod(elfs, 2)
            ncount = cd[0]
#     lastelf = n-1

print "elfs left", elfs
print "LAST ELF", lastelf, f(n, None)

