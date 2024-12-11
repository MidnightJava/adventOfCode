from collections import defaultdict

grid = {}
amap = defaultdict(list)
antinodes = set()
dim = 0

def get_slope(l1, l2):
  return (l2[0] - l1[0], l2[1] - l1[1]) # (ydiff, xdiff)

def get_pairs(node, slope, locs):
  pairs = []
  ydiff, xdiff = slope
  for loc in locs:
    if loc[1] - node[1] == -xdiff and loc[0] - node[0] == -ydiff:
      pairs.append((node[0] + ydiff, node[1] +  xdiff))
      pairs.append((node[0] - 2 * ydiff, node[1] - 2 * xdiff))
  return pairs
  
def get_pairs2(node, slope, locs):
  pairs = []
  ydiff, xdiff = slope
  for loc in grid:
    _xdiff = loc[1] - node[1]
    _ydiff = loc[0] - node[0]
    if _xdiff != 0 and _ydiff != 0 and ydiff / xdiff == _ydiff / _xdiff:
      pairs.append(loc)
  return pairs
      
def get_dnodes(node, locs):
  global dim
  for loc in [loc for loc in locs if loc != node]:
    slope = get_slope(loc, node)
    pairs = get_pairs(node, slope, locs)
    for pair in pairs:
      if pair[0] >= 0 and pair[0] < dim and pair[1] >= 0 and pair[1] < dim:
        antinodes.add(pair)
        
def get_dnodes2(node, locs):
  global dim
  for loc in [loc for loc in locs if loc != node]:
    slope = get_slope(loc, node)
    pairs = get_pairs2(node, slope, locs)
    for pair in pairs:
      if pair[0] >= 0 and pair[0] < dim and pair[1] >= 0 and pair[1] < dim:
        antinodes.add(pair)

with open("2024/data/day08") as f:
  for y, row in enumerate(f.readlines()):
    for x, c in enumerate(row.strip()):
      grid[(y,x)] = c
      amap[c].append((y,x))
dim = y + 1
      
for ant in [ant for ant in amap if ant != '.']:
  locs = [loc for loc in grid if grid[loc] == ant]
  for loc in locs:
    # get_hnodes(loc, locs)
    # get_vnodes(loc, locs)
    get_dnodes(loc, locs)
print(f"Part 1: {len(antinodes)}")

antinodes = set()
for ant in [ant for ant in amap if ant != '.']:
  locs = [loc for loc in grid if grid[loc] == ant]
  for loc in locs:
    get_dnodes2(loc, locs)

print(f"Part 2: {len(antinodes)}")

# Part 1: 265
# Part 2: 962
    