lines = open('day2.txt').read().split()
for i in range(len(lines)):
	for j in range(i, len(lines)):
		countDiffLetter=0
		for k in range(len(lines[i])):
			if lines[i][k] != lines[j][k]:
				countDiffLetter+=1
		if countDiffLetter==1:
			print(lines[i],lines[j])
			
		
