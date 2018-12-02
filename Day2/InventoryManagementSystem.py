from collections import *
double=0
triple=0
lines = open('day2.txt').read().split()
for line in lines:
	word = Counter(line)
	if any(count == 2 for _, count in word.items()):
		double+=1
	if any(count == 3 for _, count in word.items()):
		triple+=1

print(double*triple)
