import re
# muls = []
p = r"mul\(\-?\d{1,3}\,\-?\d{1,3}\)"
p2 = r"mul\((\-?\d{1,3})\,(\-?\d{1,3})\)"
do = r"do\(\)"
dont = r"don\'t\(\)"
total = 0

def find_muls(s):
  global total
  m = re.search(p, s)
  while m:
    mul = m.group(0)
    print(mul)
    # muls.append(mul)
    m2 = re.match(p2, mul)
    total += (int(m2.group(1)) * int(m2.group(2)))
    s = s[m.end() -1:]
    m = re.search(p, s)

def filt(s):
  segs = []
  enabled = True
  m = re.search(dont, s)
  while m:
    end = m.end()
    start = m.start()
    if enabled:
      print("enabled")
      print(f"s: {s}", end='\n\n')
      segs.append(s[: start-1])
      s = s[end:]
      print(f"new s: {s}", end='\n\n')
      m = re.search(do, s)
      if not m: break
      enabled = False
    else:
      print("disabled")
      print(f"s: {s}", end='\n\n')
      s = s[end:]
      print(f"new s: {s}", end='\n\n')
      m = re.search(dont, s)
      if not m:
        segs.append(s)
        break
      enabled = True
    loop = True
  
  return "".join(segs)

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
  # Part 2: > 71020416, < 100426483 not 100079213 not 101629183