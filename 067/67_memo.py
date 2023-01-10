memo = {}

number_tower = []
with open("number", "r") as rp:
	while True:
		line = rp.readline()
		if not line: break
		line_split = line.strip().split(" ")
		number_line = []
		for v in line_split:
			number_line.append(int(v))
		number_tower.append(number_line)

def find_max_sub(i, j):
	memo_idx_str = "%d,%d" % (i, j)
	if memo_idx_str in memo:
		return memo[memo_idx_str]
	if i == len(number_tower) - 1:
		left = 0
		right = 0
	else:
		left = find_max_sub(i + 1, j)
		right = find_max_sub(i + 1, j + 1)
	memo[memo_idx_str] = number_tower[i][j] + max(left, right)
	return memo[memo_idx_str]

print(find_max_sub(0, 0))
