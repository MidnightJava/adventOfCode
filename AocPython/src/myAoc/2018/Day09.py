'''
Created on Dec 9, 2018

@author: Mark
'''
from __future__ import print_function
from collections import defaultdict
#468 players; last marble is worth 71843 points
part1 = True

PLAYERS = 468
LAST_MARBLE = 71843
#Brute force part 2
if not part1: LAST_MARBLE*= 100


marbles = [0]
players = defaultdict(int)

next_marble = 1
current_marble = 0
player = 0

while next_marble <= LAST_MARBLE:
	if next_marble % 23 == 0:
		players[player] += next_marble
		current_marble = (current_marble - 7) % len(marbles)
		players[player] += marbles[current_marble]
		
		del marbles[current_marble]
	else:
		if len(marbles) <= 2:
			current_marble = 1
		else:
			current_marble = (current_marble + 2) % len(marbles)
		marbles.insert(current_marble, next_marble)
		
	player = (player+1) % PLAYERS
	next_marble+= 1
#
	
print("Part 1:" if part1 else "Part 2:",max(players.values()))

# Part 1: 385,820
# Part 2: 3156297594