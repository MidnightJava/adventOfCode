'''
Created on Dec 22, 2016

@author: maleone
'''
import re

import networkx as nx

MAX_DEPTH = 1000

global nodes, viable, gr, seen, Infinity

seen = set()

Infinity = float("inf")

G = nx.Graph()

class Node():
    def __init__(self, x, y, size, used, avail):
        self.x = int(x)
        self.y = int(y)
        self.size = int(size)
        self.used = int(used)
        self.avail = int(avail)
        self.depth = 0
        
    def id(self):
        return ((self.x, self.y))
    
    def neighbors(self):
        return [n for n in nodes.values() if ((n.x == self.x -1 or n.x == self.x + 1) and n.x >= 0 and n.y == self.y) or \
                ((n.y == self.y -1 or n.y == self.y + 1) and n.y >= 0 and n.x == self.x) ]
        
    def moveData(self, source, need, countOnly = False, depth = Infinity):
        if self.size < need or depth >= MAX_DEPTH:
            return 0
        if self.avail >= need:
            if not countOnly:
                source.used-= need
                source.avail+= need
                self.used+= need
                self.avail-= need
            return 1
        else:
            best = (Infinity, None)
            for n in self.neighbors():
                if n in seen or n == source:
                    continue
                seen.add(n)
                count = n.moveData(self, self.used, True, depth+1)
                if count > 0 and count < best[0]:
                    best = (count, n)
                    print "count", count
            if best[1]:
                best[1].moveData(self, self.used, False, depth+1)
            return best[0] if best[0] != Infinity else 0
        
    def __str__(self):
        return str(self.x) + "," + str(self.y)
    
    def __repr__(self):
        return str(self.x) + "," + str(self.y)
        
with open("data/day22") as f:
    nodes = {}
    viable = set()
    for line in f:
        res = re.findall("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T", line)
        if res:
            node = res[0]
            if int(node[1]) < 13:
                nodes[(int(node[0]), int(node[1]))] = Node(node[0], node[1], node[2], node[3], node[4])
#             if node[0] != 0 and node[1] == 13:
#                 seen.add(nodes[(int(node[0]), int(node[1]))])
            
for node in nodes.values():
    for n in node.neighbors():
        if n.y < 13:
            G.add_edge(node, n)
            G.add_edge(n, node)

# for n1 in nodes.values():
#     for n2 in nodes.values():
#         if n1.id() != n2.id() and n1.used != 0 and n1.used <= n2.avail:
#             viable.add((n1, n2))

# print len(viable), "viable pairs"

paths = nx.all_shortest_paths(G, nodes[(32,0)], nodes[(0,0)])

count = 0
start = nodes[(32,0)]
for path in paths:
    nlist = list(path)
    for i in xrange(1, len(nlist)):
        print "move data for node", nlist[i]
        count+= nlist[i].moveData(start, node.used, False, 1)
        start = nlist[i]
print count