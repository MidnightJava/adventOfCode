"""
The input data is a matrix of text characters.

Part 1: Count the number of instances of the word XMAS in the data, whether appearing
horizontally, vertically, or diagonally, in forward or reverse order.

Part 2: Count the number of times the following pattern occurs in the data

M.S
.A.
M.S

That is, look for instances where two diagonal instances of MAS or SAM occur in any three by three square.
"""

dim = 140

def transpose_h(data):
 _data = []
 for row in data:
   _data.append(row[::-1])
 return _data

def transpose_v(data):
 return data[::-1]

def find_h(data):
  count = 0
  for row in range(dim):
    for col in range(dim-3):
      if data[row][col:col+4] == "XMAS" or data[row][col:col+4] == "SAMX":
        count += 1
  return count
  
def find_v(data):
  count = 0
  for col in range(dim):
    for row in range(dim-3):
      word = ""
      for i in range(4):
        word += data[row+i][col]
        if word == "XMAS" or word == "SAMX":
          count += 1
  return count

def find_d1(data):
  count = 0
  for col in range(dim-3):
    for row in range(dim-3):
      word = ""
      for i in range(4):
        word += data[row+i][col+i]
        if word == "XMAS":
          count += 1
  return count

def find_d2(data):
  data = transpose_h(data)
  return find_d1(data)

def find_d3(data):
  data = transpose_v(data)
  return find_d1(data)
  
def find_d4(data):
  data = transpose_v(data)
  data = transpose_h(data)
  return find_d1(data)

with open("2024/data/day04") as f:
  count = 0
  data = f.read().split()
  count += find_h(data)
  count += find_v(data)
  count += find_d1(data)
  count += find_d2(data)
  count += find_d3(data)
  count += find_d4(data)
  print(f"Part 1: {count}")

with open("2024/data/day04") as f:
  count = 0
  data = f.read().split()
  """
    When looking at A chars in row 0 or col 0, attempting to access
    row or col -1 will not throw an exception, because python allows
    that as a reference from the end of the array.
  """
  for row in range(1, dim):
    for col in range(1, dim):
      if data[row][col] == "A":
        try:
          found = True
          c1, c2 = data[row-1][col-1],  data[row+1][col+1]
          if not ((c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M")):
            found = False
          c1, c2 = data[row+1][col-1],  data[row-1][col+1]
          if not ((c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M")):
            found = False
          if found == True: count += 1
        except:
          found = False
          continue

  print(f"Part 2: {count}")
  
 # Part 1: 2530
 # Part 2: 1921