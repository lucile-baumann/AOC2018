
changes = open('day1.txt').read().split()
result = sum(int(x) for x in changes)
print(result)
