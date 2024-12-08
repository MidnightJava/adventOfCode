start_char = '^'
up = (-1,0)
down = (1, 0)
left = (0, -1)
right = (0,1)
data = {}

def next_dir(dir):
  if dir == up: return right
  elif dir == right: return down
  elif dir == down: return left
  elif dir == left: return up

def solve1(pos, dir, visited, data):
  while True:
    y, x = pos
    pos = (y + dir[0], x + dir[1])
    if not pos in data:
      return False
    if data[pos] == '#':
      dir = next_dir(dir)
      pos = (y + dir[0], x + dir[1])
      
    visited.add(pos)

with open("2024/data/day06") as f:
  
  for row, line in enumerate(f.readlines()):
    for col, c in enumerate(line.strip()):
      data[(row, col)] = c
      
  start = [k for k, v in data.items() if v == start_char][0]
  dir = up
  visited = set([start])
  solve1(start, dir, visited, data)
  
  print(f"Part 1: {len(visited)}")
  
rows = row + 1
cols = col + 1

  
def solve2(pos, dir, visited, data):
    state = (pos, dir)
    
    while True:
        y, x = pos
        next_pos = (y + dir[0], x + dir[1])
        
        # Guard exits the grid
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) or next_pos not in data:
            return False
        
        # Obstacle handling. Use while instead of if to handle when guard runs into an obstacle corner
        while data[next_pos] == '#':
            dir = next_dir(dir)
            # Try speeding up by jumping to next obstacle
            next_pos = (y + dir[0], x + dir[1])
            if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols) or next_pos not in data:
                return False
        
            state = (next_pos, dir)
            if state in visited:
                return True  # Detect a loop within the current run
        
        visited.add(state)
        pos = next_pos

def solve3(pos, dir, visited, data, generator = False):
    visited = set()
    while True:
      y, x = pos
      pos = (y + dir[0], x + dir[1])
      if not pos in data:
        return None
      while data[pos] == '#':
        dir = next_dir(dir)
        pos = (y + dir[0], x + dir[1])
        if not pos in data:
          return None
      if pos in visited:
        continue
      visited.add(pos)
      if generator:
        yield pos
        
count = 0
            
for pos in solve3(start, up, visited, data, True):
  if data[pos] in ('#'):
    continue
  _data = data.copy()
  _data[pos] = "#"
  dir = up
  start = [k for k, v in _data.items() if v == start_char][0]
  if solve2(start, dir, set(), _data) == True:
      count += 1

print(f"Part 2: {count}")

# Part 1: 5086
# Part 2: 1770