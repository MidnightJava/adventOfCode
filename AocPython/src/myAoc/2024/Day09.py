import re
import time
from collections import Counter

def write_disk(s):
  disk = ""
  idx = 0
  file_num = 0
  for c in s:
    if idx % 2 == 0:
      l = int(c)
      for j in range(l):
        disk += f"|{file_num}|"
      file_num += 1
    else:
      free = int(c)
      for j in range(free):
        disk += "."
    idx += 1
  return disk

def fragmented(disk):
  return not re.match(r"^[^.]+\.+$", disk)

def move_next_block(disk):
  rdisk = disk[::-1]
  m = re.search(r"\|\d+\|", rdisk)
  block = m.group()
  rdisk = rdisk[:m.start()] + rdisk[m.end():]
  disk = rdisk[::-1]
  block = block[::-1]
  idx = disk.index('.')
  disk = disk[:idx] + block + disk[idx+1:]
  return disk
      

def defrag(disk):
  while fragmented(disk):
    disk = move_next_block(disk)
    # print(disk.index('.'))
  return disk

# def calculate_score(disk):
#   disk = disk.replace("|", "")
#   score = 0
#   idx = 0
#   while True:
#     m = re.search(r"\|(\d)\|", disk)
#     if not m: break
#     score += idx * int(m.group(1))
#     disk = disk[m.end():]
#     idx += 1
#   return score

def calculate_score(disk):
  disk = disk.replace("|", "")
  score = 0
  idx = 0
  for c in disk:
    if c != ".":
      score += idx * int(c)
    idx += 1
  return score

def get_file_numbers(disk):
  m = re.search(r"\|(\d+)\|$", disk)
  initial_num = int(m.group(1))
  for i in range(initial_num, -1, -1):
    yield i

    
  
# with open("2024/data/day09a") as f:
#   map = f.read()
#   start = time.time()
#   # print(f"disk map: {map}")
#   disk = write_disk(map)
#   # print(f"disk: {disk}")
#   disk  = defrag(disk)
#   # print(disk)
#   # print(disk.replace("|", ""))
#   score = calculate_score(disk)
#   print(f"Part 1: {score}, time: {time.time() - start:.0f} secs")

def move_file(n, disk):
  m1 = re.search(f"((?:\|{n}\|)+)", disk)
  num = m1.group(1).count(f"|{n}|")
  quant = "{" + f"{num}" + "}"
  m2 = re.search(f"\.{quant}", disk[:m1.start()])
  if m2:
    blocks = m1.group(1)
    disk = disk[:m1.start()]   + '.' * num + disk[m1.end():]
    disk = disk[:m2.start()] + blocks + disk[m2.end():]
  return disk

with open("2024/data/day09") as f:
  map = f.read()
  start = time.time()
  # print(f"disk map: {map}")
  disk = write_disk(map)
  # print(f"disk: {disk}")
  for i in get_file_numbers(disk):
    disk = move_file(i, disk)
  score = calculate_score(disk)
  print(f"Part 2: {score}, time: {time.time() - start:.0f} secs")
  # Part 1: 6337367222422

  '|0||0||9||9||2||1||1||1||7||7||7|.|4||4|.|3||3||3|....|5||5||5||5|.|6||6||6||6|.....|8||8||8||8|..'