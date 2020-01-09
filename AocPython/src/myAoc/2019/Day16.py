from itertools import cycle

# inp = open('2019/data/day16').read()
# for n in range(100):
#     outp  = ''
#     for j in range(1, len(inp)+1):
#         tot = 0
#         pattern = cycle([0,1,0,-1])
#         p = next(pattern)
#         for i in range(1, len(inp)+1):
#             if i % j == 0: p = next(pattern)
#             tot+= (int(inp[i-1]) * p)
#         outp+= str(tot)[-1]
#     inp = outp

# print('Part 1: %s' % outp[:8])

inp = open('2019/data/day16').read()
offset = int(inp[:7])
inp = (inp * 10000)[offset:]
for n in range(100):
    tot = sum(map(int, list(inp)))
    outp, subtr  = '', 0
    for j in range(len(inp)):
        outp+= str(tot - subtr)[-1]
        subtr+= int(inp[j])
    inp = outp
print('Part 2: %s' % inp[:8])

#Part 1: 27831665
#Part 2: 36265589