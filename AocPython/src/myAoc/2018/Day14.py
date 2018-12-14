'''
Created on Dec 14, 2018

@author: Mark
'''
import string

TARGET = 360781
TARGET = '360781'
# TARGET = '59414'

tlist = [3,6,0,7,8,1]
# tlist = [5,1,5,8,9]
# tlist = [9,2,5,1,0]
# tlist = [5,9,4,1,4]
# TARGET = 9

recipes = [3,7]

current = [0,1]

def find_sub_list(sl,l):
	sll=len(sl)
	for ind in (i for i,e in enumerate(l) if e==sl[0]):
		if l[ind:ind+sll]==sl:
			return ind

# while len(recipes) < TARGET + 10:
# 	n = recipes[current[0]] + recipes[current[1]]
# 	ns = str(n)
# 	nsd = int(ns.strip(string.ascii_letters))
# 	for c in str(nsd):
# 		recipes.append(int(c))
# 	current[0] = (current[0] + 1 + recipes[current[0]]) % len(recipes)
# 	current[1] = (current[1] + 1 + recipes[current[1]]) % len(recipes)
	
done = False
ntarget = TARGET
while not done:
	n = recipes[current[0]] + recipes[current[1]]
	ns = str(n)
	nsd = int(ns.strip(string.ascii_letters))
	for c in str(nsd):
		recipes.append(int(c))
		if c == ntarget[0]:
			ntarget = ntarget[1:]
			if len(ntarget) == 0:
				idx = find_sub_list(tlist, recipes)
				if idx:
					print idx
					break
					done = True
			
		else:
			ntarget = TARGET
	current[0] = (current[0] + 1 + recipes[current[0]]) % len(recipes)
	current[1] = (current[1] + 1 + recipes[current[1]]) % len(recipes)
	
# 	s = ''.join(map(lambda x: str(x), recipes))
# 	try:
# 		idx = s.index(TARGET)
# 		print idx
# 		done = True
# 	except ValueError:
# 		pass
	
# 	idx = find_sub_list(tlist, recipes)

# 	idx = 0
# 	found = True
# 	for i in tlist:
# 		j = 0
# 		try:
# 			old_idx = idx
# 			idx = recipes.index(i)
# 			if j == 0:
# 				found_idx = idx
# 			j+= 1
# 			if idx - old_idx != 1:
# 				found = False
# 				break
# 		except ValueError:
# 			found = False
# 			break
# 		
# 			
# 	if found:
# 		print(found_idx)
# 		done = True
		
		
# print recipes[-10:]
	