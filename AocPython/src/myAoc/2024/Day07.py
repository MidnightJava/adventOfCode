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
    bits = bin(i)[2:].zfill(n-1)
    ops = list(map(lambda x: "+" if x == '0' else "*", list(bits)))
    op = ops.pop(0)
    results = set()
    if op == "+":
      results.add(_equation[0] + _equation[1])
      results.add(int(str(_equation[0]) + str(_equation[1])))
    elif op =="*":
      results.add(_equation[0] * _equation[1])
      results.add(int(str(_equation[0]) + str(_equation[1])))
    idx = 2
    for op in ops:
      results2 = results.copy()
      if op == "+":
        for r in results:
         results2.add(r + _equation[idx])
         results2.add(int(str(r) + str(_equation[idx])))
      elif op =="*":
        for r in results:
          results2.add(r *_equation[idx])
          results2.add(int(str(r) + str(_equation[idx])))
      results = results2
      idx += 1
    for r in results:
      if res == r: return res
  return 0

def evaluate3(res, equation, results):
  # if len(equation) == 1 and len(results) == 0:
  #   return res if equation == res else 0
  if not len(equation):
    if not len(results):
      print("No results")
    else:
      for r in results:
        if r == res:
          return res
      return 0
  if not len(results):
    results.add(equation[0])
    return evaluate3(res, equation[1:], results)
  else:
    results2 = results.copy()
    for r in results:
      results2 = set(filter(lambda x: x != r, results2))
      results2.add(r + equation[0])
      results2.add(r * equation[0])
      results2.add(int(str(r) + str(equation[0])))
    return evaluate3(res, equation[1:], results2)

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
  

with open("2024/data/day07") as f:
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

# for k,v in data.items():
#   res = evaluate2(k, v)
#   if res != 0: print(f"Res {res}")
#   score += res
  
for k,v in data.items():
  equation = list(map(lambda x: int(x), v))
  res = evaluate3(k, equation, set())
  if res != 0: print(f"Res {res}")
  score += res

print(f"Part 2: {score}")

# Part 1: 3749
# Part 2: x < 97903014900743 x > 23172614