
fact = {}
fact[1] = 1
fact[0] = 1
def factorial(n):
	if n in fact:
		return fact[n]
	return n * factorial(n - 1)

cnt = 0
for n in range(1, 101):
	for r in range(n + 1):
		comb = factorial(n) / factorial(r) / factorial(n - r)

		if comb > 1000000:
			cnt += 1

print(cnt)
