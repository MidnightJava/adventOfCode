from itertools import product
from time import time

data = {}

def add(a, b): return a + b
def mult(a, b): return a * b
def concat(a, b): return int(f"{a}{b}")

def evaluate(res, equation):
  n = len(equation)
  if n == 1: return res if int(equation[0]) == res else 0
  for i in range(2**(n-1)):
    _equation = list(map(lambda x: int(x), equation[::]))
    bits = bin(i)[2:].zfill(n-1)
    ops = list(map(lambda x: "+" if x == '0' else "*", list(bits)))
    op = ops.pop(0)
    _res = 0
    if op == "+":
      _res = _equation.pop(0) + _equation.pop(0)
    elif op =="*":
      _res = _equation.pop(0) * _equation.pop(0)
    for op in ops:
      if op == "+":
        _res += _equation.pop(0)
      elif op =="*":
        _res *= _equation.pop(0)  
    if res == _res:
      return res
  return 0

def evaluate2(test, operands):
  perms = list(product([1,2,3], repeat=len(operands) - 1))
  for perm in perms:
    _operands = operands[::]
    res = _operands.pop(0)
    for i, op in enumerate(_operands):
      if perm[i] == 1: res = add(res, op)
      elif perm[i] == 2: res = mult(res, op)
      elif perm[i] == 3: res = concat(res, op)
    if res == test: return test
  return 0

with open("2024/data/day07") as f:
  for line in f.readlines():
    parts = line.strip().split(":")
    data[int(parts[0].strip())] = parts[1].split()

start = time()
score = 0
for k,v in data.items():
  res = evaluate(k, v)
  score += res
  
print(f"Part 1: {score},  {time() - start:.2f} secs")

score = 0

start = time()
for k,v in data.items():
  equation = list(map(lambda x: int(x), v))
  res = evaluate2(k, equation)
  score += res

print(f"Part 2: {score}, {time() - start:.2f} secs")

# Part 1: 3749
# Part 97902809384118