"""
The input represents numerous bingo boards, expressed as a five-by-five
matrix of numbers, and a series of numbers that represent the numbers called
during a bingo game. Players win only with veritical or horizontal patterns.
Diagonal lines do not count. A score is calculated for the winning board as:
The sum of the nubers in the squares that were NOT called, multiplied by the
last number that was called, resulting in the win.

Part 1: Find the first board that wins and calculate its score.

Part 2: Find the last board that wins and calculate its score.

Provide a "Part" argument of 1 (default) or 2
"""

import sys
from collections import defaultdict

idx = defaultdict(set)
boards = []

def transpose(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

def find_winner():
    for i in range(len(boards)):
        if i in wins: continue
        board = boards[i]
        for l in board:
            if -1 in l and len(set(l)) == 1:  return i
        board = transpose(board)
        for l in board:
            if -1 in l and len(set(l)) == 1: return i
    return None

def mark_board(num, bnum):
    board = boards[bnum]
    for l in board:
        for i in range(len(board)): l[i] = -1 if l[i] == num else l[i]
        winner = find_winner()
        if winner is not None: return winner
    return None

with open('2021/data/day04') as f:
    board = None
    got_numbers = False
    bnum = -1
    for l in [l.strip() for l in f.readlines()]:
        if not got_numbers:
            numbers = map(lambda x: int(x), l.split(','))
            got_numbers = True
        elif not len(l):
            if board: boards.append(board)
            board = []
            bnum+= 1
        else:
            row = list(map(lambda x: int(x), l.split()))
            for n in row: idx[n].add(bnum)
            board.append(row)
    boards.append(board)

wins = set()
if len(sys.argv) >= 2:
    part = sys.argv[1]
else:
    part = "1"

if part == "1":
    for n in numbers:
        for b in idx[n]:
            winner = mark_board(n, b)
            if winner: break
        if winner: break
elif part == "2":
    for n in numbers:
        for b in idx[n]:
            if b in wins: continue
            winner = mark_board(n, b)
            if winner is not None:
                wins.add(b)
                if len(wins) == 100:
                    break
        if len(wins) == 100:
                    break
else:
    print("Specify 1 or 2")
    sys.exit(0)

score = 0
for l in boards[winner]:
    l = map(lambda x: 0 if x == -1 else x, l)
    score+= sum(l)
score*= n

print('Part %s:  %d' % (part, score))

# Part : 16674
# Part 2: 7075
