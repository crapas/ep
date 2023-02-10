import math

prime = [2]

def is_prime(n):
	if n == 1:
		return False
	if n in prime:
		return True
	else:
		for i in range(2, int(math.sqrt(n) + 1)):
			if n % i == 0:
				return False
	prime.append(n)
	return True

def find_under_prime(n):
	prime_list = []
	for i in range(2, n):
		if is_prime(i):
			prime_list.append(i)
	return prime_list

def is_gold(n):
	prime_list = find_under_prime(n)
	for p in prime_list:
		test = math.sqrt((n - p) / 2)
		if test == int(test):
			print(f"{n} = {p} + 2 * {test} ^ 2")
			return True
	return False

i = 1
while True:
	test = i * 2 + 1
	if not is_prime(test) and not is_gold(test):
		print(test)
		break
	i += 1
