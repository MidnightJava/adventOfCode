"""
Input is a series of code lines that include matching open/close characters which
demarcate chunks.

Part 1: Find corrupted lines, i.e. lines where a non-matching close character is found.
Increase the  score ny the designated amount assinged to each close character.

Part 2: Discard corrupted lines, and now find incomplete lines. i.e. lines with open chunks.
Add close characters in the appropriate order to close all chunks. Keep track of score by 
multiplying the current score by five then adding the score amount assinged to the close
character. Record the score for each line, sort the list of scores, and report the middle
score (there will be an odd number of scores).
"""

code = []
remove= []
stack = []

opens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
closes = {
    ')': [3, 1],
    ']': [57, 2],
    '}': [1197, 3],
    '>': [25137, 4]
}

score = 0
f = open('2021/data/day10')
for line in f.readlines():
    code.append(line.strip())

for line in code:
    for c in line:
        if c in opens.keys():
            stack.append(c)
        elif c in closes.keys():
            if not len(stack) or opens[stack.pop()] != c:
                score+= closes[c][0]
                remove.append(line)
                break

print('Part 1: %d' % score)

for line in remove: code.remove(line)
scores = []

for line in code:
    stack = []
    for c in line:
        if c in opens.keys():
            stack.append(c)
        elif c in closes.keys():
            if opens[stack.pop()] != c:
                print("Unexpected character on stack or empty stack")
    score = 0
    while len(stack) > 0:
        cc = opens[stack.pop()]
        score*= 5
        score+= closes[cc][1]
    scores.append(score)

scores = sorted(scores)
score = scores[(len(scores) + 1) / 2 - 1]

print('Part 2: %d' % score)


# Part 1: 394647
# Part 2: < 2797840607