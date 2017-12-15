'''
Created on Dec 14, 2017

@author: Mark
'''

seed_a = 679
seed_a = 65
seed_b = 771
seed_b = 8921
factor_a = 16807
factor_b = 48271
divisor = 2147483647

count = 0
loop = 0
# for i in xrange(40000000):
# 	
# 	seed_a = int((float(seed_a) * float(factor_a)) % divisor)
# 	seed_b = int((float(seed_b) * float(factor_b)) % divisor)
# 	
# 	bin_a =  bin(seed_a)[2:].zfill(4)
# 	bin_b =  bin(seed_b)[2:].zfill(4)
# 	
# 	if loop <= 5:
# 		print seed_a
# 		print seed_b
# 		print bin_a
# 		print bin_b
# 		print
# 	
# 	if bin_a[len(bin_a) - 16: len(bin_a)] == bin_b[len(bin_b) - 16: len(bin_b)]:
# 		count+=1
# 		
# 	if loop % 1000000 == 0:
# 		print "Loop", loop
# 	loop+= 1
# print "Part 1:", count

stack_a = []
stack_b = []
while True:
	
	seed_a = int((float(seed_a) * float(factor_a)) % divisor)
	if seed_a % 4 == 0 and len(stack_a) < 5000000:
		bin_a = bin(seed_a)[2:].zfill(4)
		stack_a.append(bin_a[len(bin_a) - 16: len(bin_a)])
	
	seed_b = int((float(seed_b) * float(factor_b)) % divisor)
	if seed_b % 8 == 0 and len(stack_b) < 5000000:
		bin_b = bin(seed_b)[2:].zfill(4)
		stack_b.append(bin_b[len(bin_b) - 16: len(bin_b)])
		
	if len(stack_a) == 5000000 and len(stack_b) == 5000000:
		break
	
	if len(stack_a) % 10000 == 0:
		print "Stacks", len(stack_a), len(stack_b)

loop = count = 0
while len(stack_a) > 0:
	if stack_a.pop(0) == stack_b.pop(0)[len(bin_b) - 16: len(bin_b)]:
		count+= 1
	if loop % 10000 == 0:
		print "Loop2", loop
	loop+= 1
print "Part 2:", count
	
#not 1224