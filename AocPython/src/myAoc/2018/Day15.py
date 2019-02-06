
def print_grid():
    for y in range(h):
        for x in range(w):
            print(grid[(x,y)], end='')
        print()

def get_actors():
    l = []
    for y in range(h):
        for x in range(w):
            if grid[(x,y)] == 'G' or grid[(x,y)] == 'E':
                l.append((x,y))
    return l

with open('./data/Day15a') as f:
    global grid, hits
    grid = {}
    hits = {}
    y = 0
    for line in f:
        x = 0
        for c in line:
            grid[(x,y)] = c
            hits[(x,y)] = 200
            x+= 1
        y+= 1
    w = x
    h = y

def find_shortest_path(s, d):
    a = 1

def reading_order(paths):
    ymin = h
    xmin = w
    path = None
    for p in paths:
        if path == None or (p[1] <= ymin and p[0] < xmin):
            xmin = p[0], ymin = p[1]
            path = list(p)
    return path

def move(loc):
    subj = grid[loc)]
    enemy = 'G' if subj == 'E' else 'E'
    shortest_paths = []
    splen = None
    for target in get_actors():
        if grid[target] == enemy:
            path = find_shortest_path(loc, grid[target])
            if not shortest_paths or len(path) < splen:
                shortest_paths = [list(path)]
                splen = len(sp)
            elif len(path) == splen:
                shortest_paths.append(path)
            
    if len(shortest_paths) == 1:
        next_loc = shortest_paths[0][0]
    else:
        next_loc = reading_order(shortest_paths)[0]
    grid[loc)] = '.'
    grid[next_loc] = subj

print_grid()

def tick():
    actors = get_actors()
    print(actors)
    for actor in actors:
        move(actor)

done = False
while not done:
    tick()
    done = True


