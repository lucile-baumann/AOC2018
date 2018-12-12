# Advent of code 2018
# --- Day 9: Marble Mania ---
from collections import defaultdict


players = 463
points = 71787
scores = defaultdict(int) # default value of int is 0
marbles = [0, 1]
index = 1

for i in range(2, points+1):
	player = i % (players)
	if i % 23 == 0:
		scores[player] += i
		removeIdx = (index-7)%len(marbles)
		scores[player]+= marbles[removeIdx]
		del marbles[removeIdx]
		index=removeIdx
	else:
		index = (index+2)%len(marbles)
		if index == 0:
			index = len(marbles)
		marbles.insert(index,i)
print(max(scores.values()))

# Part two
points = 71787*100

scores = defaultdict(int) # default value of int is 0
marbles = list([0, 1])
index = 1

for i in range(2, points+1):
	player = i % (players)
	if i % 23 == 0:
		scores[player] += i
		removeIdx = (index-7)%len(marbles)
		scores[player]+= marbles[removeIdx]
		del marbles[removeIdx]
		index=removeIdx
	else:
		index = (index+2)%len(marbles)
		if index == 0:
			index = len(marbles)
		marbles.insert(index,i)
print(max(scores.values()))

