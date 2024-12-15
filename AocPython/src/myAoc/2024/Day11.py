stones = []
n_blinks = 25
stones = []
results = []

def parse(l):
  return list(map(int, l.split()))

def next_stone(stone):
  if stone == 0: return [1]
  if len(str(stone)) % 2 == 0:
    mid = int(len(str(stone)) / 2)
    s1 = int(str(stone)[:mid])
    s2 = int(str(stone)[mid:])
    return [s1, s2]
  else: return [stone * 2024]
  
def blink(stones):
  doubles = 0
  _stones = stones[::]
  j = 0
  for i, stone in enumerate(stones):
    k = i +j
    new_stones = next_stone(stone)
    if len(new_stones) == 1:
      _stones[k] = new_stones[0]
    elif len(new_stones) == 2:
      _stones[k] = new_stones[0]
      _stones.insert(k+1, new_stones[1])
      j += 1
      doubles += 1
    else:
      print(f"Error: {len(new_stones)} created")
  return _stones, (doubles, len(stones))

with open("2024/data/day11") as f:
  stones = parse(f.read().strip())
    
_stones = stones[::]
for i in range(n_blinks):
  _stones, doubles = blink(_stones[::])
  results.append(len(_stones))
  prev = 0 if i  == 0 else results[i-1]
print(f"Part 1: {len(_stones)}")

n_blinks = 75

def get_stone_count(stone, total, reps, seen):
  # print(f"rep {reps}")
  if reps == n_blinks:
    # print(f"Returning {total} after {reps} reps")
    return total
  stones = next_stone(stone)
  # total = len(stones)
  reps += 1
  for stone in stones:
    if stone in seen:
      total += seen[stone]
    else:
      _total = get_stone_count(stone, total, reps, seen)
      seen[stone] = _total
      total += _total
    # print(f"Total so far: {total}\n\n")
  return total


score = 0
for stone in stones:
  score += get_stone_count(stone, 0, 0, {})
  # print(score)
print(f"Part 2: {score}")


"""
All stones will be either 0, 1, or a multiple of 2024, until they reach an even number of
digits and split. Find a pattern in multiples of 2024 having an even number of digits.
"""


# Part 1: 194782
# Part 2: x > 179492722309546 x > 182452461385176 x < 271304679931354