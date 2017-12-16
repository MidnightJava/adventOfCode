'''
Created on Dec 14, 2017

@author: Mark
'''

divisor = 2147483647

def get_next(seed, mod, factor, part2):
	count = 0
	while True:
		seed = seed * factor % divisor
		count+= 1
		if count % 5000000 == 0 and (part2 or mod == 4):
			print "{}Gen count: {} million".format("\t\t\t" if part2 and mod == 8 else "", count/1000000)
		if not part2 or seed % mod == 0:
			yield seed & 0xffff

count = 0
gena = get_next(679, 4, 16807, False)
genb = get_next(771, 8, 48271, False)
for _ in xrange(40000000):
	if gena.next() == genb.next():
		count+=1
print "Part 1:", count

count = 0
gena = get_next(679, 4, 16807, True)
genb = get_next(771, 8, 48271, True)
for _ in xrange(5000000):
	if gena.next() == genb.next():
		count+=1
print "Part 2:", count
