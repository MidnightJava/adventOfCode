'''
Created on Dec 14, 2018

@author: Mark
'''
import string
import time

target = 360781
recipes = [3,7]
current = [0,1]

start_time = time.time()
while len(recipes) < target + 10:
	n = recipes[current[0]] + recipes[current[1]]
	ns = str(n)
	nsd = int(ns.strip(string.ascii_letters))
	for c in str(nsd):
		recipes.append(int(c))
	current[0] = (current[0] + 1 + recipes[current[0]]) % len(recipes)
	current[1] = (current[1] + 1 + recipes[current[1]]) % len(recipes)
print 'Part 1:', ''.join(map(lambda x: str(x), recipes[-10:])), 'time: %d sec' % (time.time() - start_time)


#### Part 2 ####

target = str(target)
done = False
ntarget = target
start_time = time.time()
while not done:
	n = recipes[current[0]] + recipes[current[1]]
	n_digits = str(n).strip(string.ascii_letters)
	for c in n_digits:
		recipes.append(int(c))
		if c == ntarget[0]:
			ntarget = ntarget[1:]
			if not ntarget:
				print 'Part 2:', len(recipes) - len(target), 'time: %d sec' % (time.time() - start_time)
				done = True
				break

		else:
			ntarget = target
	current[0] = (current[0] + 1 + recipes[current[0]]) % len(recipes)
	current[1] = (current[1] + 1 + recipes[current[1]]) % len(recipes)

# Part 1: 6521571010
# Part 2: 20262967


