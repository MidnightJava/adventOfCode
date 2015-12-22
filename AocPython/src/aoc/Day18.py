'''
Created on Dec 18, 2015

@author: Mark
'''
lights = [[],[]]
part2 = False
def nextState(row, line, current):
    newLine = "*"
    for col in xrange(1, len(line) -1):
        numOn = 0
        numOn = sum([1 for r in xrange(row -1, row+2) for c in xrange(col -1, col +2) if  not (c == col and r == row)
                     and lights[current][r][c] == "#"])
        if part2 and ((row == col == 1) or (row == col == 100) or (row == 1 and col == 100) or (row == 100 and col == 1)):
            newLine += "#"
        elif line[col] == '#':
            newLine += "#" if numOn == 2 or numOn == 3 else "."
        else:
            newLine += "#" if numOn == 3 else "."
    newLine += "*"
    return newLine

def init():    
    with(open("lights.txt")) as f:
        lights[0].append("*" * 102)
        for line in f:
            lights[0].append("*" + line.strip() + "*")
        lights[0].append("*" * 102)
        lights[1] = lights[0][::-1]

def run():
    init()
    curr = 0
    for i in xrange(0, 100):
        for row in xrange(1, 101):
            lights[1 - curr][row] = nextState(row, lights[curr][row], curr)
        curr = 1 - curr
    
    count = sum([s.count("#")  for s in lights[curr]])
    print count, "lights on"

run()
part2 = True
lights = [[],[]]
run()