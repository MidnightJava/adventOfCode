data = {}

def evaluate(res, equation):
  # print(f"{' '.join(equation)}")
  n = len(equation)
  claz = type(equation[0])
  eq = int(equation[0])
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

def evaluate2(res, equation):
  n = len(equation)
  if n == 1: return res if int(equation[0]) == res else 0
  for i in range(2**(n-1)):
    _equation = list(map(lambda x: int(x), equation[::]))
    _equation2 = list(map(lambda x: int(x), equation[::]))
    _equation3 = list(map(lambda x: int(x), equation[::]))
    bits = bin(i)[2:].zfill(n-1)
    ops = list(map(lambda x: "+" if x == '0' else "*", list(bits)))
    op = ops.pop(0)
    _res = 0
    _res2 = 0
    _res3 = 0
    if op == "+":
      _res = _equation.pop(0) + _equation.pop(0)
      _res2 = int(str(_equation2.pop(0)) + str(_equation2.pop(0)))
      _res3 = int(str(_equation.pop(0)) + str(_equation2.pop(0)))
    elif op =="*":
      _res = _equation.pop(0) * _equation.pop(0)
      _res2 = int(str(_equation2.pop(0)) + str(_equation2.pop(0)))
    for op in ops:
      if op == "+":
        _res += _equation.pop(0)
        _res2 = int(str(_res2) + str(_equation2.pop(0)))
      elif op =="*":
        _res *= _equation.pop(0)
        _res2 = int(str(_res2) + str(_equation2.pop(0)))
    if res == _res or res == _res2:
      return res
  return 0

# concact item 0 with the rest, then items 0and 1 with the rest, etc.
def concat_options(eq):
  n = len(eq)
  if n == 1: return [eq]
  res = []
  for i in range(2**(n-1)):
    _eq = eq[::]
    bits = bin(i)[2:].zfill(n-1)
    s = _eq.pop(0)
    for b in list(bits):
      if b == '1': s += " "
      s+= _eq.pop(0) 
    res.append(s.split())
  return res

  

# def evaluate2(res, equation):
#   # print(f"{' '.join(equation)}")
#   for equation in concat_options(equation):
#     n = len(equation)
#     if n == 1: return equation if int(equation) == res else 0
#     for i in range(2**(n-1)):
#       _equation = list(map(lambda x: int(x), equation[::]))
#       bits = bin(i)[2:].zfill(n-1)
#       ops = list(map(lambda x: "+" if x == '0' else "*", list(bits)))
#       op = ops.pop(0)
#       _res = 0
#       if op == "+":
#         _res = _equation.pop(0) + _equation.pop(0)
#       elif op =="*":
#         _res = _equation.pop(0) * _equation.pop(0)
#       for op in ops:
#         if op == "+":
#           _res += _equation.pop(0)
#         elif op =="*":
#           _res *= _equation.pop(0)  
#       if res == _res:
#         return res
#     return 0
  

with open("2024/data/day07a") as f:
  for line in f.readlines():
    parts = line.strip().split(":")
    data[int(parts[0].strip())] = parts[1].split()

score = 0
for k,v in data.items():
  # print(f"{k} = {v}")
  res = evaluate(k, v)
  score += res
  
print(f"Part 1: {score}")

score = 0
# for k,v in data.items():
#   # print(f"{k} = {v}")
#   opts = concat_options(v)
#   for equation in opts:
#     res = evaluate(k, equation)
#     score += res

for k,v in data.items():
  res = evaluate2(k, v)
  score += res

print(f"Part 2: {score}")

# Part 1 x > 358332626678