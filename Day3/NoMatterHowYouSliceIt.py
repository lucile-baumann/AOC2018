# Advent of Code 2018 
# --- Day 3: No Matter How You Slice It ---

allClaimsID=[]
grid = {}
count = 0
lines = open('day3.txt').readlines()
for line in lines:
	claimID, claimInfos = line.strip().split(" @ ")
	allClaimsID.append(claimID)
	coords, dim = claimInfos.split(": ")
	x, y = [int(n) for n in coords.split(",")]
	w, h = [int(k) for k in dim.split("x")]
	for i in range(x, x+w):
		for j in range(y, y+h):
			if (i,j) not in grid:
				grid[(i,j)]=[]
			grid[(i,j)].append(claimID)

for coord, data in grid.items():
	if len(data) > 1:
		count+=1

print(count)
print(len([data for _, data in grid.items() if len(data) > 1]))

# --- Part Two ---
setClaim = set(allClaimsID)
for claims in grid.values():
	if len(claims)>=2:
		setClaim=setClaim.difference(claims)
print(setClaim)
