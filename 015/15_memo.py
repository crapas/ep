
x = 20
y = 20
memo = {}

def cal_path(x, y):
	if x == 0:
		return 1
	if y == 0:
		return 1
	if x * 100 + y not in memo:
		memo[x * 100 + y] = cal_path(x - 1, y) + cal_path(x, y - 1)
	return memo[x * 100 + y]

print(cal_path(x, y))
