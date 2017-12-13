'''
Created on Dec 12, 2017

@author: Mark
'''

layers = {}
cost = 0
caught = False

with open("data/Day13") as f:
	for line in f:
		x = line.strip().split(":")
		layers[int(x[0].strip())] = int(x[1].strip())

for i in xrange(max(layers.keys())+1):
	if i in layers:
		r = layers[i]
		if i % (2*r - 2) == 0:
			caught = True
			cost+= (i * r)

print "Part 1", cost

#Optimization based on data: (0:3, 1:2)
delay = -2
while True:
	delay+= 4
	cost = 0
	caught = False
	for i in xrange(delay, max(layers.keys())+1 + delay):
		j = i - delay
		if j in layers:
			r = layers[j]
			if i % (2*r - 2) == 0:
				caught = True
				cost+= (i * r)
				break
# 	if delay % 100000 == 0:
# 		print "testing delay", delay
	if not caught:
		print "Part 2:", delay
		break
