'''
Created on Dec 21, 2016

@author: maleone
'''

numelfs = 3004953

# numelfs = 11

# After failing to get a solution by generating a number series, got the idea
# of a circular linked list from a subreddit help thread.

class Elf():

    def __init__(self, iden):
        self.iden = iden
        self.next = None
        self.prev = None
        
    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next

def initElfs():
    global elfs
    elfs = []
    elfs = map(Elf, xrange(numelfs))
    for i in xrange(numelfs):
        elfs[i].next = elfs[(i+1) % numelfs]
        elfs[i].prev = elfs[(i-1) % numelfs]

def part1():
    initElfs()
    elf = elfs[0]
    while (elf.next):
        elf.next.remove()
        if elf.next == elf:
            elf.next = None
        else:
            elf = elf.next
        
    print "Part 1", elf.iden + 1 #because we numbered the elves from 0 instead of 1
    
def part2():
    initElfs()
    elf = elfs[0]
    nextElf = elfs[numelfs / 2]
    for i in xrange(numelfs -1):
        nextElf.remove()
        nextElf = nextElf.next
        if (numelfs -i) % 2 == 1:
            nextElf = nextElf.next
        elf = elf.next
        
    print "Part 2", elf.iden + 1
    
part1()
part2()