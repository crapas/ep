import math
prime = {}
def is_prime(n):
	if n in prime:
		return prime[n]
	for i in range(2, int(math.sqrt(n) + 1)):
		if n % i == 0:
			prime[n] = False
			return False
	prime[n] = True
	return True

def is_prime_pair(n1, n2):
	t1 = int(str(n1) + str(n2))
	t2 = int(str(n2) + str(n1))
	if is_prime(t1) and is_prime(t2):
		return True
	else:
		return False

prime_list = [3]
i = 0
j = 4
prime_cnt = 1
pair_list = []
triple_list = []
quad_list = []
penta_list = []

while True:
	while not is_prime(j):
		j += 1
	print("TEST : %d" % j)
	for q in quad_list:
		if is_prime_pair(q[0], j) and is_prime_pair(q[1], j) and is_prime_pair(q[2], j) and is_prime_pair(q[3], j):
			penta_list.append(q[0], q[1], q[2], q[3], j)
		break
	for t in triple_list:
		if is_prime_pair(t[0], j) and is_prime_pair(t[1], j) and is_prime_pair(t[2], j):
			quad_list.append((t[0], t[1], t[2], j))
			print("Add Quad %d :" % len(quad_list), quad_list[-1])
	for p in  pair_list:
		if is_prime_pair(p[0], j) and is_prime_pair(p[1], j):
			triple_list.append((p[0], p[1], j))
	
	for i in prime_list:
		if is_prime_pair(i, j):
			pair_list.append((i, j))

	prime_list.append(j)
	j += 1
	if j > 100000:
		break

print(pair_list)
print("---")
print(triple_list)
print("---")
print(quad_list)
print("---")
print(penta_list)
#print(prime_list)
