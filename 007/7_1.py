import math

cnt = 10001
i = 2
prime = []

def prime_check(n):
	if n < 2:
		return False
	if n == 2:
		return True
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

while True:
	if prime_check(i):
		prime.append(i)
	if len(prime) == cnt:
		break
	i += 1

print(prime[-1])

