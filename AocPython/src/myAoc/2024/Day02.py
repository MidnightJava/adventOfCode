
"""
  Each line of the input is a report with numeric values separated by spaces.
  
  Part 1:
  Determine the number of "safe" reports, where a report is safe if both of the following conditions are true:
    1) All values are decreasing or all values are increasing
    2) The difference between all adjacent values is between 1 and 3 inclusive
  
  Part 2:
  Determine the number of safe reports with the same creiteria as in Part 1, except:
    - Consider a report safe if it meets the creiteria of Part 1 when any single value of the report is removed.
"""

count = 0

def is_safe(line):
  rpt = map(lambda x: int(x), line.split())
  prev = None
  dir = None
  safe = True
  for val in rpt:
    if prev is None:
      prev = val
      continue
    _dir = 1 if val - prev > 0 else -1
    if dir is None:
      dir = _dir
    else:
      safe = False if dir != _dir else safe
    diff = abs(val - prev)
    safe = False if diff < 1 or diff > 3 else safe
    prev = val
  return safe
      
  
with open('2024/data/day02') as f:
  for line in f:
   if is_safe(line.strip()): count += 1
print(f"Part 1: {count}")
   
count = 0
with open('2024/data/day02') as f:
  for line in f:
    for i in range(len(line.split())):
      vals = line.split()
      del vals[i]
      if is_safe(' '.join(vals)):
        count += 1
        break
      
print(f"Part 2: {count}")

# Part 1: 383
# Part 2: > 436