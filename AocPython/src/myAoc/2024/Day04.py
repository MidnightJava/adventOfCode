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
      if data[row][col:col+4] == "XMAS":
        count += 1
  print(f"h count {count}")
  return count
  
def find_hr(data):
  data = transpose_h(data)
  count = find_h(data)
  print(f"hr count {count}")
  return count
  
def find_v(data):
  count = 0
  for col in range(dim):
    for row in range(dim-3):
      word = ""
      for i in range(4):
        word += data[row+i][col]
        if word == "XMAS":
          count += 1
  print(f"v count {count}")
  return count
  
def find_vr(data):
  data = transpose_v(data)
  count = find_v(data)
  print(f"vr count {count}")
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
  print(f"d1 count {count}")
  return count

def find_d2(data):
  data = transpose_h(data)
  count = find_d1(data)
  print(f"d2 count {count}")
  return count

def find_d3(data):
  data = transpose_v(data)
  count = find_d1(data)
  print(f"d3 count {count}")
  return count
  
def find_d4(data):
  data = transpose_v(data)
  data = transpose_h(data)
  count = find_d1(data)
  print(f"d4 count {count}")
  return count

with open("2024/data/day04") as f:
  count = 0
  data = f.read().split()
  count += find_h(data)
  count += find_hr(data)
  count += find_v(data)
  count += find_vr(data)
  count += find_d1(data)
  count += find_d2(data)
  count += find_d3(data)
  count += find_d4(data)
  print(f"Part 1: {count}")
  
 # Part 1: x> 2520