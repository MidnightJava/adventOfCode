import re
import time

def write_disk1(s):
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
  return disk

def calculate_score1(disk):
   score = 0
   idx = 0
   while True:
     m = re.search(r"\|(\d+)\|", disk)
     if not m: break
     score += idx * int(m.group(1))
     disk = disk[m.end():]
     idx += 1
   return score


def calculate_score(disk):
  score = 0
  for k, v in disk.items():
    if v > 0:
      score += k * v
  return score

def get_file_numbers(disk):
  unique_nums = set(filter(lambda x: x >= 0, disk.values()))
  nums = sorted(unique_nums, reverse=True)
  for n in nums: yield n
   
with open("2024/data/day09") as f:
  map = f.read()
  start = time.time()
  # print(f"disk map: {map}")
  disk = write_disk1(map)
  # print(f"disk: {disk}")
  disk  = defrag(disk)
  # print(disk)
  # print(disk.replace("|", ""))
  score = calculate_score1(disk)
  print(f"Part 1: {score}, time: {time.time() - start:.0f} secs")

def write_disk(s):
  disk = {}
  read_idx = 0
  write_idx = 0
  file_num = 0
  for c in s:
    if read_idx % 2 == 0:
      l = int(c)
      for j in range(l):
        disk[write_idx] = file_num
        write_idx += 1
      file_num += 1
    else:
      free = int(c)
      for j in range(free):
        disk[write_idx] = -1
        write_idx += 1
    read_idx += 1
  return dict(sorted(disk.items()))

def move_file(filenum, disk):
  locs = sorted([n for n in disk.keys() if disk[n] == filenum])
  size = len(locs)
  for i in range(len(disk)):
    if i > locs[0]: break
    if all(disk[loc] == -1 for loc in range(i,  i + size)):
      for loc in locs:
        disk[loc] = -1
      for j in range(i, i + size):
        disk[j] = filenum
      break
  return disk

def show_disk(disk):
  return ''.join([ '.' if v == -1 else str(v) for v in disk.values() ])

with open("2024/data/day09") as f:
  map = f.read()
  start = time.time()
  disk = write_disk(map)
  for n in get_file_numbers(disk):
    disk = move_file(n, disk)
  # print(f"final expanded disk:\t{show_disk(disk)}")
  score = calculate_score(disk)
  print(f"Part 2: {score}, time: {time.time() - start:.0f} secs")
  # Part 1: 6337367222422
  # Part 2: 6361380647183

