from collections import deque
from collections import defaultdict

d = defaultdict(list)

for line in open('2021/data/day12').readlines():
    parts = map(lambda x: x.strip(), line.split('-'))
    d[parts[0]].append(parts[1])
    d[parts[1]].append(parts[0])

num_paths = 0
queue = deque([['start']])

while queue:
    path = queue.popleft()
    node = path[-1]
    if node == 'end':
        num_paths+= 1
        continue
    for nbr in d[node]:
        if nbr.isupper() or nbr not in path: queue.append(path+[nbr])

print('Part 1: %d' % num_paths)


def can_visit(node, path):
    if node.isupper(): return True
    if node == 'start' or node == 'end': return node not in path
    counts = defaultdict(int)
    for n in [n for n in path if n.islower()]: counts[n]+= 1
    if 2 in counts.values():
        return node not in path
    else:
        return True
       

num_paths = 0
queue = deque([['start']])

while queue:
    path = queue.popleft()
    node = path[-1]
    if node == 'end':
        num_paths+= 1
        continue
    for nbr in d[node]:
        if can_visit(nbr, path):
            queue.append(path+[nbr])

print('Part 2: %d' % num_paths)

# Part 1: 4573
# Part 2: 117509
