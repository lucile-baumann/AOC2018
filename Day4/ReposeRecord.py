# Advent Of Code 2018
# --- Day 4: Repose Record ---
from datetime import datetime


lines = open('day4.txt').readlines()
for line in lines:
	time = datetime.strptime(line[0:18],"[%Y-%m-%d %H:%M]")
	data = line[19:]
	print(time)
