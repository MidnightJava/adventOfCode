'''
Created on Dec 17, 2016

@author: Mark
'''
import md5, copy

lplen = 0
spath = []
splen = 1e6
paths = []
passw = "bwnlcvfs"
        
def opened(digest):
    return [False if int(x, 16) <= 10 else True for x in digest[:4]]

def move(state):
    nextstates = []
    md = md5.new()
    md.update(state["pass"] + state["path"])
    doors = opened(md.hexdigest().upper())
    i = state["id"]
    if doors[0]: #up
        st = copy.copy(state)
        if i > 4:
            st["id"] = i - 4
            st["path"]+= "U"
            nextstates.append(st)
    if doors[1]: #down
        st = copy.copy(state)
        if i <= 12:
            st["id"] = i + 4
            st["path"]+= "D"
            nextstates.append(st)
    if doors[2]: #left
        st = copy.copy(state)
        if not i in [1,5,9,13]:
            st["id"] = i - 1
            st["path"]+= "L"
            nextstates.append(st)
    if doors[3]: #right
        st = copy.copy(state)
        if i % 4 != 0 :
            st["id"] = i + 1
            st["path"]+= "R"
            nextstates.append(st)
            
    return nextstates

def solve(state):
    global paths
    if state["id"] == 16:
        paths.append(state["path"])
        return
    for st in move(state):
        solve(st)
    
state = {"id": 1, "path":"", "pass": passw}
solve(state)

for path in paths:
    if len(path) < splen:
        splen = len(path)
        spath = path
    if len(path) > lplen:
        lplen = len(path)
print "shortest path", spath
print "Longest path length:", lplen
        