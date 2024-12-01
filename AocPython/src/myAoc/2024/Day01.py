"""
  The input represents two lists, with one item of each list on each line.
  
  Part 1:
  Pair up the smallest number in the left list with the smallest number in the right list,
  then the second-smallest left number with the second-smallest right number, and so on.

  Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
  
  Part 2:
  Determine exactly how often each number from the left list appears in the right list. Calculate a total
  similarity score by adding up each number in the left list after multiplying it by the number of times
  that number appears in the right list.
"""

from collections import Counter

l1 = []
l2 = []
l1a = []
l1a = []
l2a = []

d = 0
s = 0

with open('2024/data/day01') as f:
  for line in f:
   e1, e2 = map(lambda x: int(x), line.split())
   l1.append(e1)
   l2.append(e2)
   
l1a = l1[::]
c = Counter(l2)
for i in range(len(l1)):
  m1 = min(l1)
  m2 = min(l2)
  d += abs(m2 - m1)
  l1.remove(m1)
  l2.remove(m2)
  s+= l1a[i] * int(c[l1a[i]])
print(f"part 1: {d}")
print(f"Part 2: {s}")
# Part 1: 1506483
# Part 2: 23126924