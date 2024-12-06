start_char = '^'
up = (-1,0)
down = (1, 0)
left = (0, -1)
right = (0,1)
visited = set()

def next_dir(dir):
  if dir == up: return right
  elif dir == right: return down
  elif dir == down: return left
  elif dir == left: return up

def move(pos, dir, data):
  y, x = pos
  next = (y + dir[0], x + dir[1])
  if next[0] < 0 or next[0] >= len(data) or next[1] < 0 or next[1] >= len(data[0]):
    return None, None
  if data[next[0]][next[1]] == '#':
    dir = next_dir(dir)
    next = (y + dir[0], x + dir[1])
  if next[0] < 0 or next[0] >= len(data) or next[1] < 0 or next[1] >= len(data[0]):
    return None
  visited.add(next)
  return next, dir



def current_loc(data):
  for row in range(len(data)):
    for col in range(len(data[row])):
      if data[row][col] == start_char:
        return (row, col)

with open("2024/data/day06") as f:
  count = 0
  data = f.read().split()
  curr = current_loc(data)
  dir = up
  visited.add(curr)
  while curr is not None:
    curr, dir = move(curr, dir, data)

print(f"Part 1: {len(visited)}")