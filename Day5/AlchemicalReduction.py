# Advent of Code 2018
# --- Day 5: Alchemical Reduction ---

data = open('day5.txt').read().strip()
i=0
while i<len(data)-1:
	#ord return the unicode code of a char 
	if abs(ord(data[i])-ord(data[i+1]))==32:
		# remove the part
		if i==len(data)-1:
			data =data[:i]
		else:
			data =data[:i]+data[i+2:]
			i = max(0, i-1)
	else:
		i+=1

print(len(data))