import sys

global grid
grid = []
global count
count = 0
global seen
seen = set()

def print_grid():
    for row in grid: print(row)

def flashable():
    global grid
    for row in grid:
        for c in row:
            if c>= 10: return True
    return False


def flash():
    global count
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 10:
                if (row,col) not in seen: count+= 1
                seen.add((row,col))
                grid[row][col] = 0
                for y in [row-1, row, row+1]:
                    for x in [col-1, col, col+1]:
                        if y>=0 and x >=0 and (y,x) != (row,col):
                            try:
                                grid[y][x]+= 1
                            except IndexError:
                                pass
                
    # if flashable(): flash()
    # print_grid()

f = open('2021/data/day11a')
for line in f:
    grid.append(map(lambda x: int(x), line.strip()))

for step in range(100):
    global seen
    seen = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 10:
                print("ERROR")
                sys.exit()
            grid[row][col]+= 1

    # Try flashiing recursivvely again, this time allowing values past 10 and keeping track of flashed for each step.

    while flashable(): flash()
    

        
    if step <= 5:
        print('After STEP %d' % (step+1))
        print_grid()

print('Part 1: %d' % count)
# Part 1: < 1983