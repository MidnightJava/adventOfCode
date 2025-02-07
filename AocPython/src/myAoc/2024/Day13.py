from itertools import islice, product
import re
import math

from math import gcd, floor, ceil

def extended_gcd(a, b):
    """Extended Euclidean Algorithm: Returns (g, x, y) such that g = gcd(a, b) and ax + by = g"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

def find_minimum_a(c1, c2, c3):
    """Finds the integer solution (a, b) with the smallest a for a*c1 + b*c2 = c3."""
    g, x0, y0 = extended_gcd(c1, c2)

    # Check if the equation has integer solutions
    if c3 % g != 0:
        return None  # No integer solution exists
    
    # Scale the initial solution
    scale = c3 // g
    a0 = x0 * scale
    b0 = y0 * scale

    # Step to adjust `a` for minimization
    step = c2 // g  # Step size for a in the general solution

    # Find the smallest `a` by choosing `k`
    k_min = -floor(a0 / step)  # This chooses the smallest positive `a`
    a_min = a0 + k_min * step
    b_min = b0 - k_min * (c1 // g)

    return (a_min, b_min)

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
  solution = find_minimum_a(a[0], b[0], target[0])
  print(f"a: {a} b: {b} target: {target}")
  if solution:
    print(f"solution: {solution}")
    print(f"caclulated target: {(a[0]* solution[0], b[0]* solution[1])}")
    solution2 = find_minimum_a(a[1], b[1], target[1])
    if solution2:
      total += (3 * solution[0] + solution[1])
      print(f"solution2: {solution2}")
      print(f"caclulated target: {(a[1]* solution2[0], b[1]* solution2[1])}")
    
    
# # print(f"Part 2: {total}")
# c1, c2, c3 = 34, 67, 10000000005400
# solution = find_minimum_a(c1, c2, c3)
# if solution:
#     print(f"Minimum a solution found: a = {solution[0]}, b = {solution[1]}")
# else:
#     print("No integer solution exists.")



# Part 1:
# Part 2: 29877
# x < 4342237642345787
# x < 141216321806444 
# x > 87110658696094
#     558400153034
#     1571376573209