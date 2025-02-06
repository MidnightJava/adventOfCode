from itertools import islice, product
import re

data = []

min_score = None

def read_lines(file):
    while True:
        lines = list(islice(file, 4))
        if not lines:
            break
        yield lines[:3]

with open("2024/data/day13a") as f:
  for lines in read_lines(f):
    m = re.match(r"Button A\: X\+(\d+), Y\+(\d+)", lines[0])
    a = (int(m.group(1)), int(m.group(2)))
    m = re.match(r"Button B\: X\+(\d+), Y\+(\d+)", lines[1])
    b = (int(m.group(1)), int(m.group(2)))
    m = re.match(r"Prize\: X\=(\d+), Y\=(\d+)", lines[2])
    target = (int(m.group(1)), int(m.group(2)))
    data.append({"a": a, "b": b, "target": target})

total = 0
for rec in data:
  (a, b, target) = (rec["a"], rec["b"], rec["target"])
  perms = product(range(100), repeat=2)
  scores = []
  for perm in perms:
    x = a[0] * perm[0] + b[0] * perm[1]
    y = a[1] * perm[0] + b[1] * perm[1]
    if (x,y) == target:
      score = 3 * perm[0] + perm[1]
      scores.append(score)
  if len(scores): total += min(scores)
    
print(f"Part 1: {total}")

total = 0
for rec in data:
  (a, b, target) = (rec["a"], rec["b"], rec["target"])
  target = (target[0] + 10000000000000, target[1] + 10000000000000)
  i = j = 0
  done = False
  while not done:
    i += 1
    while not done:
      j += 1
      if i * a[0] + j * b[0] == target[0] and i * a[1] + j * b[1] == target[1]:
        total += (j + 3 * i)
        done = True
        print('done 1')
        break
      elif  i * a[0] + j * b[0] > target[0] or i * a[1] + j * b[1] > target[1]:
        done = True
        print('done 2')
        break
    
    
print(f"Part 2: {total}")
# max_mod = None
# for rec in data:
#   (a, b, target) = (rec["a"], rec["b"], rec["target"])
#   target = (target[0] + 10000000000000, target[1] + 10000000000000)
#   ax = divmod(target[0], a[0])
#   ay = divmod(target[1], a[1])
#   bx = divmod(target[0], b[0])
#   by = divmod(target[1], b[1])
#   if ax[1] == 0 and ay[1] == 0 and bx[1] == 0 and by[1] == 0:
#      max_mod = max(max_mod, ax[0], ay[0], bx[0], by[0])

# for rec in data:
#   (a, b, target) = (rec["a"], rec["b"], rec["target"])
#   perms = product(range(max_mod), repeat=2)
#   scores = []
#   for perm in perms:
#     x = a[0] * perm[0] + b[0] * perm[1]
#     y = a[1] * perm[0] + b[1] * perm[1]
#     if (x,y) == target:
#       score = 3 * perm[0] + perm[1]
#       scores.append(score)
#   if len(scores): total += min(scores)
    
# print(f"Part 2: {total}")
    