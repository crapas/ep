import math

prime = []

def is_prime(n):
	if n in prime:
		return True
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	prime.append(n)
	return True

def is_permutted(n1, n2, n3):
	n1_str = str(n1)
	n2_str = str(n2)
	n3_str = str(n3)
	n1_arr = []
	n2_arr = []
	n3_arr = []
	for c in n1_str:
		n1_arr.append(c)
	for c in n2_str:
		n2_arr.append(c)
	for c in n3_str:
		n3_arr.append(c)
	if sorted(n1_arr) == sorted(n2_arr) and sorted(n2_arr) == sorted(n3_arr):
		return True
	else:
		return False

for i in range(1000, 10000):
#for i in range(1486, 1488):
	if not is_prime(i):
		continue
	j = 1
	while True:
		c1 = i + j
		c2 = i + j * 2
		j += 1
#		print(i, c1, c2)
		if c2 > 9999:
			break
		if not is_prime(c1) or not is_prime(c2):
			continue
		if not is_permutted(i, c1, c2):
			continue
		print("%d%d%d" % (i, c1, c2))
