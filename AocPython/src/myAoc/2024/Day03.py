import re
# muls = []
p = r"mul\(\-?\d{1,3}\,\-?\d{1,3}\)"
p2 = r"mul\((\-?\d{1,3})\,(\-?\d{1,3})\)"
do = "do()"
dont = "don't()"
dodont =r"do\(\)|don\'t\(\)"
total = 0

def find_muls(s):
  global total
  m = re.search(p, s)
  while m:
    mul = m.group(0)
    # print(mul)
    m2 = re.match(p2, mul)
    total += (int(m2.group(1)) * int(m2.group(2)))
    s = s[m.end() -1:]
    m = re.search(p, s)

# def filt(s):
#   s2 = ""
#   enabled = True
#   start = 0
#   cand = ""
#   print(f"Original s: {s}", end='\n\n')
#   for m in re.finditer(dodont, s):
#     print(f"result: {m.group()}")
#     if enabled:
#       print("enabled")
#       if m.group() == do:
#         start = m.end()
#         print(f"New start: {start}")
#         print(f"s: {s[start:]}", end='\n\n')
#       elif m.group() == dont:
#         s2 += s[start: m.start()]
#         print(f"s2: {s2}", end='\n\n')
#         start = m.end()
#         print(f"New start: {start}", end='\n\n')
#         print(f"s: {s[start:]}", end='\n\n')
#         enabled = False
#     else:
#       print("Not enabled")
#       if m.group() == do:
#         start = m.end()
#         print(f"New start: {start}", end='\n\n')
#         print(f"s: {s[start:]}", end='\n\n')
#         enabled = True
        
def filt(s):
  # print('\n\n')
  s2 = ""
  enabled = True
  start = 0
  cand = ""
  prev = dont
  # print(f"Original s: {s}", end='\n\n')
  for m in re.finditer(dodont, s):
    # print(f"result: {m.group()}")
    op = m.group()
    if op == do:
      if prev == do:
        start = m.end()
        # print(f"New start: {start}")
        # print(f"s: {s[start:]}", end='\n\n')
      elif prev == dont:
        s2 += cand
        cand = ""
        start = m.end()
    elif op == dont:
      if prev == do:
        cand = s[start: m.start()]
        # start = m.end()
      elif prev == dont:
        cand = s[start: m.start()]
        # start = m.end()

    prev = op
    # print("new loop", end='\n\n')

  
  if op == do:
    s2 += s[start:]
  else:
    # cand += s[start:]
    s2 += cand
  
  return s2

# with open('2024/data/day03') as f:
#   for line in f:
#     find_muls(line)
#   print(f"Part 1: {total}")
  
total = 0
with open('2024/data/day03') as f:
  for line in f:
    line = filt(line.strip())
    find_muls(line)
  print(f"Part 2: {total}")
  
  # Part 1: 174103751
  # Part 2: > 71020416, < 100426483 not 100079213 101629183  913656786 676478962 51913388 62681101 74179637 74112610 85611146