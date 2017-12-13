'''
Created on Dec 12, 2017

@author: Mark
'''

layers = {}
pos = {}
sense = {}
cost = 0
caught = False
with open("data/test") as f:
	for line in f:
		x = line.strip().split(":")
		layers[int(x[0].strip())] = int(x[1].strip())
		pos[int(x[0].strip())] = 0
		sense[int(x[0].strip())] = 0
	layersorig = layers.copy()
	posorig = pos.copy()
	senseorig = sense.copy()
	
for i in xrange(max(layers.keys())+1):
	if i in pos:
		if pos[i] == 0:
			caught = True
			cost+= (i * layers[i])
	for k,v in pos.items():
		if sense[k] == 0:
			pos[k] = (v+1)
			if pos[k] == (layers[k] -1):
				sense[k] = 1
		else:
			pos[k] = (v-1)
			if pos[k] == 0:
				sense[k] = 0
print "Part 1", cost

delay = 0
while True:
	delay+= 1
	count = 1
	cost = 0
	caught = False
	sense = senseorig
	pos = posorig
	loc = -1
	for i in xrange(max(layers.keys())+1):
		if count > delay:
			loc+= 1
			if loc in pos:
				if pos[loc] == 0:
					caught = True
					cost+= (loc * layers[loc])
					break
		for k,v in pos.items():
			if sense[k] == 0:
				pos[k] = (v+1)
				if pos[k] == (layers[k] -1):
					sense[k] = 1
			else:
				pos[k] = (v-1)
				if pos[k] == 0:
					sense[k] = 0
		count+=1
	if not caught:
		print "Part 2:", delay
		break

#not 3, 4, 99, 98
#try 100
	