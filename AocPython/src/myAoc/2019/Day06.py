from collections import defaultdict

_map = {}
seen = set()
with open('2019/data/day06') as f:
    for line in f:
        kv = line.split(')')
        _map[kv[1].strip()] = kv[0]

# Part 1
def solve(node, res):
    while node:
        if _map.get(node, None):
            node = _map[node]
            res['count']+= 1
            if not node in seen:
                solve(node, res)
            seen.add(node)
        else:
            node = None

leaves = set(_map.keys()) - set(_map.values())
res = {'count': 0}
for node in leaves:
    solve(node, res)
print('Part 1: %d' % res['count'])

#Part 2
def mk_path(node):
    path = []
    while node:
        if _map.get(node, None):
            node = _map[node]
            path.append(node)
        else:
            return path

you_path = mk_path('YOU')
san_path = mk_path('SAN')

for n in you_path:
    n = _map.get(n)
    if n in san_path:
        print('Part 2: %d' % (you_path.index(n) + san_path.index(n)))
        break

# Part 1: 402879
# Part 2: 484