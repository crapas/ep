memo = {}
def ispandigital(n_str):
	if n_str in memo:
		return memo[n_str]

	check = []
	for i in range(0, 10):
		check.append(False)
	check[0] = True

	for c in n_str:
		check[int(c)] = True
	if False in check:
		memo[n_str] = False
		return False
	else:
		memo[n_str] = True
		return True

	return False
pm = []
for i in range(1, 500000000):
	if i % 10000000 == 0:
		print("=== > %d" % i)
	j = 2
	cat_str = str(i)
	while True:
		cat_str += str(i * j)
		if len(cat_str) == 9:
			if ispandigital(cat_str):
				print(cat_str)
				pm.append(int(cat_str))
		if len(cat_str) > 9:
			break
		j += 1

print(max(pm))
