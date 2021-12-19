"""
Input represents a grid of points. The number for each point locaiton is its height,
one through nine. FOr purposes of the puzzle adjacent points are those directly above,
below, to the right, or to the left of a given point. Diagonal adjaceny is ignored.

Part 1: Find all low points, i.e. points where all adjacent points are higher than it. Rerturn
the sum of the risk levels ofall low points, where risk level is a points height plus one.

Part 2: Basins are defined as all the points that drain into the same low point. For every
low point there will be exactly one basin. Find all the basins and compute their size as the
number of points in the basin,including the low point. Return the product of the size of the three
largest basins.
"""

f = open('2021/data/day09')
grid =[]
lps = []
for line in f.readlines():
    grid.append(map(lambda x: int(x), list(line.strip())))

score = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        low = True
        for y,x in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            try:
                if grid[y][x] <= grid[r][c]:
                    low = False
                    break
            except IndexError:
                pass
        if low:
            lps.append((r,c))
            score+= (1 + grid[r][c])

print('Part 1: %d' % score)

seen = set()

def discover_basin(pt, count):
    global seen
    seen.add(pt)
    r,c = pt
    for y,x in [(y,x) for (y,x) in [(r-1, c), (r+1, c), (r, c-1), (r,c+1)] if y >= 0 and x >= 0]:
        try:
            if (y,x) not in seen and grid[y][x] > grid[r][c] and grid[y][x] != 9:
                count+= discover_basin((y,x), 0)
        except IndexError:
            pass
    count+= 1
    
    return count

basins = []
for lp in lps:
    basins.append(discover_basin(lp, 0))

basins = sorted(basins)
score= 1
for i in [1,2,3]:score*= basins[-i]
print('Part 2: %d' % score)

# Part 1: 566
# Part 2: 891684