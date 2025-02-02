from collections import deque

grid = {}
starts = set()
region_list = []

with open("2024/data/day12") as f:
  for row, line in enumerate(f.readlines()):
    for col, c in enumerate(line.strip()):
      grid[(row, col)] = c
      
width = col +1
height = row + 1

def get_perim(region, locs):
  perim = 0
  global grid
  for (y,x) in locs:
    neighbors = [n for n in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]]
    for n in neighbors:
      if not n in grid or grid[n] != region: perim+= 1
  return perim

def get_perim2(region, locs):
  perim = 0
  global grid
  for y in range(height):
    start_fence = False
    for x in range(width):
      if not (y,x) in locs:
        if start_fence: perim += 1
        start_fence = False
        continue
      if grid[(y,x)] == region:
        if (y-1,x) not in grid or grid[(y-1,x)] != region:
          start_fence = True
        else:
          if start_fence:
            start_fence = False
            perim += 1
    if start_fence: perim += 1
    start_fence = False
    for x in range(width):
      if not (y,x) in locs:
        if start_fence: perim += 1
        start_fence = False
        continue
      if grid[(y,x)] == region:
        if (y+1,x) not in grid or  grid[(y+1,x)] != region:
          start_fence = True
        else:
         if start_fence:
          start_fence = False
          perim += 1
    if start_fence: perim += 1
            
  start_fence = False
  for x in range(width):
    start_fence = False
    for y in range(height):
      if not (y,x) in locs:
        if start_fence: perim += 1
        start_fence = False
        continue
      if grid[(y,x)] == region:
        if (y,x-1) not in grid or grid[(y,x-1)] != region:
          start_fence = True
        else:
          if start_fence:
            start_fence = False
            perim += 1
    if start_fence: perim += 1
    start_fence = False
    for y in range(height):
      if not (y,x) in locs:
        if start_fence: perim += 1
        start_fence = False
        continue
      if grid[(y,x)] == region:
        if (y, x+1) not in grid or grid[(y,x+1)] != region:
            start_fence = True
        else:
          if start_fence:
            start_fence = False
            perim += 1
    if start_fence: perim += 1
  
  return perim

def get_region(y, x):
    global grid
    global starts
    global region_list
    region = grid[(y,x)]
    regions = set([(y,x)])
    queue = deque( [(y,x)])
    
    while len(queue):
      y,x = queue.popleft()
      neighbors = [n for n in [(y, x-1), (y, x+1), (y-1, x), (y+1, x)] if n in grid and grid[n] == region and n not in regions]
      for nb in neighbors:
          starts.add(nb)
          regions.add(nb)
          queue.append((nb[0],nb[1]))
    if len(regions): region_list.append({region: regions})
          
for y in range(height):
  for x in range(width):
    if not (y,x) in starts:
      get_region(y, x)

cost = 0
for region in region_list:
  k,v = list(region.items())[0]
  cost += len(v) * get_perim(k,v)

print(f"Part 1: {cost}")

cost = 0
for region in region_list:
  k,v = list(region.items())[0]
  cost += len(v) * get_perim2(k, v)

print(f"Part 2: {cost}")
  
# Part 1: 1467094
# Part 2: 881182
