data = {}

def evaluate(res, equation):
  # print(f"{' '.join(equation)}")
  n = len(equation)
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

def concat_list(l):
  res = []
  n = len(l)
  for i in range(2**(n-1)):
    _l = list(map(lambda x: int(x), l[::]))
    bits = bin(i)[2:].zfill(n-1)
    ones = [i for i, b in enumerate(bits) if b == '1']
    for i in range(1, len(_l)):
      if i in ones:
        res.append(_l[i-1] + _l[i])
        i += 1
      else:
        res.append(_l[i])
  return res

  

def evaluate2(res, equation):
  # print(f"{' '.join(equation)}")
  for equation in concat_list(equation):
    n = len(equation)
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
for k,v in data.items():
  # print(f"{k} = {v}")
  res = evaluate2(k, v)
  score += res
  
print(f"Part 2: {score}")

# Part 1 x > 358332626678