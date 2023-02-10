solution_cnt = {}

for n in range(4, 1001):
	exceed = False
	for a in range(1, n):
		for b in range(a, n):
			c = n - a - b
			if c < 1:
				break
			if c >= a + b:
				continue
			if c <= a or c <= b:
				break
			if c ** 2 == a ** 2 + b ** 2:
				print(a, b, c, a + b + c)
				if a + b + c not in solution_cnt:
					solution_cnt[a + b + c] = 1
				else:
					solution_cnt[a + b + c] += 1

s_max = 0
key = -1
for k, v in solution_cnt.items():
	if v > s_max:
		key = k
		s_max = v

print(solution_cnt)
print(key, s_max)

	
