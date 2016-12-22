'''
Created on Dec 21, 2016

@author: Mark
'''
import re

indexmap = {"0":1, "1":1, "2": 6, "3":2, "4":7, "5":3, "6":0, "7":4}

def p(pword, line):
    global indexmap
    res = re.findall("swap position (\d) with position (\d)", line)
    if res:
        res = res[0]
        a = int(res[0]) if int(res[0]) < int(res[1]) else int(res[1])
        b = int(res[1]) if int(res[0]) < int(res[1]) else int(res[0])
            
        pword = pword[:a] + pword[b] + pword[a+1: b] + pword[a] + pword[b + 1:]
    else:
        res = re.findall("swap letter (\w+) with letter (\w+)", line)
        if res:
            res = res[0]
            pword = pword.replace(res[0], "*").replace(res[1], res[0]).replace("*", res[1])
        else:
            res = re.findall("rotate (left|right) (\d+)", line)
            if res:
                res = res[0]
                t = ""
                for i in range(len(pword)):
                    a = 1 if res[0] == 'left' else -1
                    a = -a if part2 else a
                    t+=pword[(i + a*int(res[1])) % len(pword)]
                pword = t
            else:
                res = re.findall("rotate based on position of letter (\w)", line)
                if res:
                    if part2:
                        index = indexmap[str(pword.index(res[0]))]
                    else:
                        index = pword.index(res[0])
                        index = index+2 if index >= 4 else index+1
                    a = 1 if not part2 else -1
                    t = ""
                    for i in range(len(pword)):
                        t+=pword[(i - a*index) % len(pword)]
                    pword = t
                    
                else:
                    res = re.findall("reverse positions (\d) through (\d)", line)
                    if res:
                        res = res[0]
                        pword = pword[:int(res[0])] + pword[int(res[0]): int(res[1]) + 1][::-1] + pword[int(res[1]) + 1:]
                    else:
                        res = re.findall("move position (\d) to position (\d)", line)
                        if res:
                            res = res[0]
                            a = int(res[1]) if part2 else int(res[0])
                            b = int(res[0]) if part2 else int(res[1])
                            w = pword[a]
                            pword = pword.replace(w, "")
                            l = list(pword)
                            l.insert(b, w)
                            pword = "".join(l)
    return pword

with open("data/day21") as f:
    global part2
    pword ="abcdefgh"
    data = []
    part2 = False
    for line in f:
        data.append(line)
        pword = p(pword, line)
    print "Part 1", pword
    part2 = True
    pword ="fbgdceah"
    for line in data[::-1]:
        pword = p(pword, line)
    print "Part 2", pword