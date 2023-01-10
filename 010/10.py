import math

upper = 2000000
i = 2
sum = 0

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
		sum += i
	if i == upper:
		break
	i += 1

print(sum)

