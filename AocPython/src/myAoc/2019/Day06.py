from collections import defaultdict

_map = {}
seen = set()
count = 0
with open('2019/data/day06') as f:
    for line in f:
        kv = line.split(')')
        _map[kv[1].strip()] = kv[0]
    # print(_map)

leaves = set(_map.keys()) - set(_map.values())
# print(leaves)

# Part 1
def solve(node):
    global count
    while node:
        if _map.get(node, None):
            node = _map[node]
            count+= 1
            if not node in seen:
                solve(node)
            seen.add(node)
        else:
            node = None

for node in leaves:
    solve(node)
print('Part 1: %d' % count)

paths = defaultdict(list)
def mk_path(node):
    global paths
    start = node
    while node:
        if _map.get(node, None):
            node = _map[node]
            paths[start].append(node)
        else:
            node = None

def get_dist(node, dest):
    count = 0
    while node:
        if _map.get(node, None):
            node = _map[node]
            count+= 1
            if node == dest:
                node = None
        else:
            node = None
    return count

#Part 2
mk_path('YOU')
mk_path('SAN')

for n in paths['YOU']:
    n = _map.get(n)
    if n in paths['SAN']:
        print('Part 2: %d' % (get_dist(_map.get('YOU'), n) + get_dist(_map.get('SAN'), n)))
        break