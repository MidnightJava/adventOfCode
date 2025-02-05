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

with open("2024/data/day13") as f:
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
  target = (target[0] * 10000000000000, target[1] * 10000000000000)
  """
  If a and b both divide evenly into target on the x and ye axes, you know you can win the prize.
  Then use the largest of the a and be modulus results above in the product call, i.e. product(range(max_modulus), repeat=2)
  """
    
print(f"Part 2: {total}")
    