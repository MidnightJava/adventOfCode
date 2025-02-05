from collections import defaultdict

n_blinks = 25
stones = None

def parse(l):
  global stones
  stones = defaultdict(int, {int(item): 1 for item in l.split()})

def next_stone(stone):
  if stone == 0: return [1]
  if len(str(stone)) % 2 == 0:
    mid = int(len(str(stone)) / 2)
    s1 = int(str(stone)[:mid])
    s2 = int(str(stone)[mid:])
    return [s1, s2]
  else: return [stone * 2024]
  
def blink(stones):
  new_stones = defaultdict(int)
  for k, v in stones.items():
    for stone in next_stone(k):
      new_stones[stone] += v
  return new_stones

for i, n in enumerate([25, 75]):
  with open("2024/data/day11") as f:
    parse(f.read().strip())
  for j in range(n):
    stones = blink(stones)
  print(f"Part {i+1}: {sum(stones.values())}")


# Part 1: 194782
# Part 2: 233007586663131