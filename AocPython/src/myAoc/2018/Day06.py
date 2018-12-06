'''
Created on Dec 6, 2018

@author: maleone
'''
nodes = {}
seen = set()

def mdist(a,b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def findFiniteAreaNodes(nodes):
	res = []
	for n1 in nodes:
		infinite = [True, True, True, True]
		for n2 in nodes:
			if n2 != n1:
				if n2[0] < n1[0]:
					infinite[0] = False
				if n2[0] > n1[0]:
					infinite[1] = False
				if n2[1] < n1[1]:
					infinite[2] = False
				if n2[1] > n1[1]:
					infinite[3] = False
		if not any(infinite):
			res.append(n1)
	return res

with open('./data/Day06') as f:
	for l in f:
		pt = l.strip().split(',')
		nodes[(int(pt[0]), int(pt[1]))] = ""

	finite = findFiniteAreaNodes(nodes)
	for node in finite:
		print node
	print len(finite)
	
	distances = {}
	for n1 in nodes:
		for n2 in nodes:
			distances[(n1, n2)] = mdist(n1,n2)
	for k,v in distances.items():
		print k,v
			
			