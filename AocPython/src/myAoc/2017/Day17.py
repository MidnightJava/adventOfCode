'''
Created on Dec 17, 2017

@author: Mark
'''
import time


step = 386
idx = 0
l = []
idx = 0
for i in xrange(2018):
	if i != 0:
		idx = (idx + step + 1) % len(l)
	l.insert(idx, i)
print "Part 1:", l[(idx + 1) % len(l)]

start = time.time()
idx = 0
l = 0
while l <= 50000000:
	ol = l
	if l != 0:
		idx = (step + 1) % l
	count = 0
	while idx != 0:
		l+= 1
		idx = (idx + step + 1) % l
		count +=1
	if l == 0:
		l =  1
	else:
		l = (count % l) + 1 + ol

print "Part 2:", (ol - 1)
print time.time() - start

#Part 1: 419

#Part2: 46038988

# l = 1227
# ol = l
# idx = (step + 1) % l
# count = 0
# while idx != 0:
# 	l+= 1
# 	idx = (idx + step + 1) % l
# 	count +=1
# print(count % l) + 1 + ol -1

# step = 386
# l = []
# idx = 0
# for i in xrange(50000000):
# 	if i != 0:
# 		idx = (idx + step + 1) % len(l)
# 	l.insert(idx, i)
# 	if i == 2017:
# 		print "Part 1:", l[(idx + 1) % len(l)]



# 	if i % 100000 == 0:
# 		print i

# print "Part 2:", l[(l.index(0) + 1) % len(l)]


