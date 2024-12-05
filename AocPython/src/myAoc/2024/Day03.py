"""
Part 1:

Parse the input and find all instances of the text "mul(n,m)", where m and n are numbers with one
to three digits. Instances of this pattern with whitespace inserted should not be selected. Find thee
result of adding up the products of the two numbers in each selected mul() statement.

Part 2:

Do the processing per Part 1, except look for do() and don't() commands in the text. ENable mul processing
when a do() command is encountered and disable processing when a don't() command is encountered. Only the
most recent do() or don't() instruction applies
"""

"""
In my solution, Part 2 incorrect, because I read "Only the most recent do() or don't() instruction applies"
as meaning that only the most recent do() or don't() instruction applies. Apparently, what is meant by that
statement is that only the most recent ONE OR MORE consecutive do() commands or ONE OR MORE consecutive don't()
commands applies. My solution applies only the most recent don't() command. So if three consecutive don't()
commands appear, it only disables mul processing after the last (most recent) one. Likewise, it only enables
processing after the last do() command when they appear consecutively.
"""
import re
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
    m2 = re.match(p2, mul)
    total += (int(m2.group(1)) * int(m2.group(2)))
    s = s[m.end():]
    m = re.search(p, s)
        
def filt(s):
  s2 = ""
  idx = 0
  cand = ""
  prev = do
  for m in re.finditer(dodont, s):
    op = m.group()
    if op == do:
      if prev == do:
        idx = m.end()
      elif prev == dont:
        s2 += cand
        cand = ""
        idx = m.end()
    elif op == dont:
      if prev == do:
        cand = s[idx: m.start()]
      elif prev == dont:
        cand = s[idx: m.start()]

    prev = op

  
  if op == do:
    s2 += s[idx:]
  else:
    s2 += cand
  return s2

with open('2024/data/day03') as f:
  for line in f:
    find_muls(line)
  print(f"Part 1: {total}")
  
total = 0
with open('2024/data/day03') as f:
  for line in f:
    line = filt(line[::])
    find_muls(line[::])
  print(f"Part 2: {total}")
  
  # Part 1: 174103751
  # Part 2: 100411201 (wrong)

"""
Chat GPT's solution, applying the correct interpretation of how to handle consecutive do() or
don't() commands
"""
  
import re

# Patterns
mul_pattern = r"mul\(\-?\d{1,3},\-?\d{1,3}\)"
mul_values_pattern = r"mul\((\-?\d{1,3}),(\-?\d{1,3})\)"
control_pattern = r"do\(\)|don't\(\)"

def find_muls(s):
    total = 0
    for m in re.finditer(mul_pattern, s):
        mul = m.group(0)
        m2 = re.match(mul_values_pattern, mul)
        total += int(m2.group(1)) * int(m2.group(2))
    return total

def filt(s):
    # Parse `do()` and `don't()` instructions
    enabled = True
    result = ""
    last_pos = 0

    for m in re.finditer(control_pattern, s):
        control = m.group()
        if enabled:
            result += s[last_pos:m.start()]  # Append enabled region
        enabled = (control == "do()")
        last_pos = m.end()
    
    # Add remaining portion if still enabled
    if enabled:
        result += s[last_pos:]
    
    return result

# Read the input and calculate the results
with open('2024/data/day03') as f:
    data = f.read()

# Part 1
total_part1 = find_muls(data)
print(f"Part 1: {total_part1}")

# Part 2
filtered_data = filt(data)
total_part2 = find_muls(filtered_data)
print(f"Part 2: {total_part2}")

# Part 1: 174103751
# Part 2: 100411201
