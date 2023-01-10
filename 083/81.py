import sys
memo = []
numbers = []
with open("number", "r") as rp:
	while True:
		line = rp.readline()
		if not line: break
		segment = line.strip().split(",")
		seg_len = len(segment)
		temp = []
		for i in range(seg_len):
			temp.append(-1)
		memo.append(temp)
		numbers.append(segment)

width = len(numbers[0])
height = len(numbers)

def find_min(x, y):
	if memo[y][x] != -1:
		return memo[y][x]
	if x == 0 and y == 0:
		return int(numbers[0][0])
	if x != 0:
		left = find_min(x - 1, y)
	else:
		left = sys.maxsize
	if y != 0:
		right = find_min(x, y - 1)
	else:
		right = sys.maxsize
	memo[y][x] = int(numbers[y][x]) + min(left, right)
	return memo[y][x]
#	return int(numbers[y][x]) + min(left, right)

v = find_min(height - 1, width - 1)

print(v)

