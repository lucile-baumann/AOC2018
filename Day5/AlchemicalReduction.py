# Advent of Code 2018
# --- Day 5: Alchemical Reduction ---

data = open('day5.txt').read().strip()

data1 = data
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

# --- Part Two ---
minimum = 9999999999
for letter in "abcdefghijklmnopqrstuvxyz":
	infos = data1
	test = infos.replace(letter,"").replace(letter.upper(),"")
	i=0
	while i<len(test)-1:
		if abs(ord(test[i])-ord(test[i+1]))==32:
			if i==len(test)-1:
				test=test[:i]
			else:
				test=test[:i]+test[i+2:]
				i = max(0, i-1)
		else:
			i+=1
	result = len(test)
	print(result)
	minimum = min(minimum, result)
print(minimum)