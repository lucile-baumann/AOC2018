lines = open('day1.txt').read().split()
output=0
freqs={0}
for x in range(0,300):
	for line in lines:
		output = output + int(line)
		if output in freqs:
			print(output)
			break
		freqs.add(output)	

