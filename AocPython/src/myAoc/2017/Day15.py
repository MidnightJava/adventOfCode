'''
Created on Dec 14, 2017

@author: Mark
'''

factors = [16807, 48271]
divisor = 2147483647
lim1 = 40000000
lim2 = 5000000

def get_seeds():
	return [679, 771]

def get_next(part2, n):
	seed = get_seeds()[n]
	mod = 4 if n == 0 else 8
	count = 0
	while True:
		seed = seed * factors[n] % divisor
		count+= 1
		if count % lim2 == 0 and (part2 or n == 0):
			print "{}Gen count: {} million".format("\t\t\t" if part2 and n == 1 else "", count/1000000)
		if not part2 or seed % mod == 0:
			yield seed & 0xffff

count = 0
gena = get_next(False, 0)
genb = get_next(False, 1)
for _ in xrange(lim1):
	if gena.next() == genb.next():
		count+=1
print "Part 1:", count

count = 0
gena = get_next(True, 0)
genb = get_next(True, 1)
for _ in xrange(lim2):
	if gena.next() == genb.next():
		count+=1
print "Part 2:", count
