import re
import time

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

def calculate_score(disk):
  score = 0
  idx = 0
  while True:
    m = re.search(r"\|(\d+)\|", disk)
    if not m: break
    score += idx * int(m.group(1))
    disk = disk[m.end():]
    idx += 1
  return score
    
  
with open("2024/data/day09") as f:
  map = f.read()
  start = time.time()
  # print(f"disk map: {map}")
  disk = write_disk(map)
  # print(f"disk: {disk}")
  disk  = defrag(disk)
  # print(disk)
  # print(disk.replace("|", ""))
  score = calculate_score(disk)
  print(f"Part 1: {score}, time: {time.time() - start:.0f} secs")
  
  # Part 1: 6337367222422