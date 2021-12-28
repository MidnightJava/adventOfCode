from __future__ import print_function
import heapq

grid = {}

y = 0
max_x = 0
max_y = 0
for line in open('2021/data/day15').readlines():
    max_y= max(max_y, y)
    line = line.strip()
    for x in range(len(line)):
        max_x = max(max_x, x)
        grid[(y,x)] = int(line[x])
    y+= 1

def heuristic(risk, curr, end):
    return abs(end[0] - curr[0]) + abs(end[1]-curr[1]) + risk

start = (0,0)
end = (max_y, max_x)
queue = [(heuristic(0, start, end), 0, start)]
visited = {}
risks = []
while queue:
    _, risk, curr = heapq.heappop(queue)
    y,x = curr
    if curr == end:
        risks.append(risk)
    if curr in visited: continue
    visited[curr] = risk
    for nbr in [n for n in [(y, x-1), (y, x+1), (y-1,x), (y+1,x)] if n in grid]:
        if not nbr in visited or visited[nbr] > risk + grid[nbr]:
            heapq.heappush(queue, (heuristic(risk + grid[nbr], nbr, end), risk + grid[nbr], nbr))

print('Part 1: %d' % min(risks))

# Part 1: 656