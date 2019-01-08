'''
Created on Jan 8, 2019

@author: maleone
'''

from __future__ import print_function
from collections import deque
import sys
sys.setrecursionlimit(18000)

depth = 6969
target = (9, 796)
# depth = 510
# target = (10, 10)
er_levels = {}
types = {}

tool = 2 # 0 = neither, 1 = climbing gear, 2 = torch

def g_idx(loc):
	if loc == (0,0) or loc == target: return 0
	elif loc[1] == 0: return loc[0] * 16807
	elif loc[0] == 0: return loc[1] * 48271
	else:
		x,y = loc
		return er_levels [(x-1, y)] * er_levels[(x, y-1)]

def can_move(curr, nxt, tool):
	if nxt[0] < 0 or nxt[1] < 0 or nxt[0] > (target[0] + 7) or (nxt[1] > target[1] + 7): return False
	x,y = curr
	if types[(x, y)] == 0: return tool > 0
	elif types[(x,y)] == 1: return tool < 2
	elif types[(x,y)] == 2: return (tool == 0 or tool == 2)
	else:
		print("Invalid region type %d" % types[(x,y)])

def valid_tools(x, y):
	rtype = types[(x,y)];
	if rtype == 0: tools = [1,2]
	elif rtype == 1: tools = [0,1]
	elif rtype == 2: tools = [0, 2]
	else: print("Invalid region type %d" % rtype)
	return tools

def update_queue(seen, queue, x, y, d, tool):
	found = False
	for item in queue:
		if item[0] == x and item[1] == y and item[3] == tool:
			if d < item[2]:
				queue[queue.index(item)] = tuple((x, y, d, tool))
			found = True
			break
	if not found and ((x,y,tool) not in seen or d < seen[(x,y,tool)]): queue.append(tuple((x, y, d, tool)))

min_vals = []
def BFS(x, y, seen, tool):
		queue = [tuple((x,y,0,tool))]
		while len(queue)>0:
# 			print(len(queue), len(seen))
			x,y,d,tool = queue.pop(0)
# 			next_locs = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if (n[0] > x and n[1] == y) or (n[1] > y and n[0] == x)]
			next_locs = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
# 			next_locs = [n for n in [(x+1,y), (x,y+1)] if n[0] < target[0] and n[1] < target[1]]
			neighbors = [n for n in next_locs if can_move((x,y), (n[0], n[1]), tool)]
			seen[(x,y,tool)] = d
# 			print('seen: %s = %d, %d' % ((x,y), d, tool))
			if (x,y) == target:
				min_vals.append(d if tool == 2 else (d+7))
				print(min(min_vals))
			for nb in neighbors:
# 				print('neighbor: %d, %d' % (n[0], n[1]))
					for new_tool in valid_tools(x, y):
						incr = 1
						if tool != new_tool:
							incr+= 7
						update_queue(seen, queue, nb[0],nb[1],d+incr,new_tool)

tot = 0
for y in xrange(target[1] + 10):
	for x in xrange(target[0] + 10):
		erosion = (g_idx((x, y)) + depth) % 20183
		er_levels[(x,y)] = erosion
		rtype = (erosion % 3)
		types[(x,y)] = rtype
		if x <= target[0] and y <= target[1]:
			tot+= rtype

for y in xrange((target[1] + 2)):
	for x in xrange((target[0] + 2)):
		if not (x,y) in types:
			erosion = (g_idx((x, y)) + depth) % 20183
			rtype = (erosion % 3)
			types[(x,y)] = rtype
		if (x,y) == target: print('X', end='')
		elif types[(x,y)] == 0: print('.', end='')
		elif types[(x,y)] == 1: print('=', end='')
		elif types[(x,y)] == 2: print('|', end='')
		else: print('illegal type %d' % types[(x,y)])
	print()
print("Part 1:", tot)

def dfs(node, visited, d):
	x,y,tool = node
	if node not in visited or d < visited[node]:
		visited[node] = d
		next_locs = [n for n in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]
		neighbors = [n for n in next_locs if can_move((x,y), (n[0], n[1]), tool)]
		if (x,y) == target:
				min_vals.append(d if tool == 2 else (d+7))
# 				print(min(min_vals))
		for n in neighbors:
			for new_tool in valid_tools(x, y):
				incr = 1
				if tool != new_tool:
					incr+= 7
				n = (n[0], n[1], new_tool)
				dfs(n, visited, d+incr)
	return visited

# visited = dfs((0,0,2), {}, 0)
# print("Part 2:", min(visited.values()))

seen = {}
BFS(0, 0, seen, tool)

print("Part 2", min(min_vals))

# Part 1: 7901
# Part 2: 2072 too high not 1123, 1109

