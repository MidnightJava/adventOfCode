from collections import deque

grid = {}

with open("2024/data/day10") as f:
  for row, line in enumerate(f.readlines()):
    for col, c in enumerate(line.strip()):
      grid[(row, col)] = int(c)
      
width = col +1
height = row + 1

def find_trails(y, x, seen):
    global grid
    trails = 0
    queue = deque( [(y,x,0)])
    while len(queue)>0:
      y,x,h = queue.popleft()
      if (y,x) not in grid:
        continue
      if h == 9:
        trails += 1
        continue
      neighbors = [n for n in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)] if n in grid]
      for nb in neighbors:
        if not nb in seen and grid[nb] == h + 1:
          seen.add(nb)
          queue.append((nb[0],nb[1],h+1))
    return trails
  
def find_unique_trails(y, x, seen):
    global grid
    start = (y,x)
    trails = set()
    queue = deque( [(y,x,[start],0)])
    while len(queue)>0:
      y,x,path,h = queue.popleft()
      if (y,x) not in grid:
        continue
      path.append((y,x))
      if h == 9:
        pathStr = ''.join(str(path))
        if pathStr in trails: continue
        trails.add(pathStr)
      neighbors = [n for n in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)] if n in grid]
      for nb in neighbors:
        if grid[nb] == h + 1:
          seen.add(nb)
          queue.append((nb[0],nb[1],path,h+1))
    return len(trails)
     
score = 0
for y in range(height):
  for x in range(width):
    if grid[(y,x)] == 0:
      score += find_trails(y, x, set())
    
print(f"Part 1: {score}")

score = 0
for y in range(height):
  for x in range(width):
    if grid[(y,x)] == 0:
      score += find_unique_trails(y, x, set())
    
print(f"Part 2: {score}")