def prime_list(n):
	primes = []
	prime_list = []
	for i in range(n + 1):
		prime_list.append(True)
	prime_list[0] = False
	prime_list[1] = False
	for j in range(2, n + 1):
		if prime_list[j]:
			primes.append(j)
		i = 1
		while True:
			if i * j > n:
				break
			prime_list[i * j] = False
			i += 1
	return primes
		
prime_list = prime_list(10000)

factor_map = {}
factor_map[1] = [1]
factor_map[2] = [1, 2]

def factor_list(n):
	if n in factor_map:
		return factor_map[n]
	factors = [1]
	i = 0
	while n != 1:
		if n % prime_list[i] == 0:
			if prime_list[i] not in factors:
				factors.append(prime_list[i])
			n = int(n / prime_list[i])
			continue
		i += 1
	return factors

def so(a, b):
	fa = factor_list(a)
	fb = factor_list(b)
	intersection_set = set(fa) & set(fb)
	if intersection_set == {1}:
		return True
	return False

def rp(n):
	rp_list = [1]
	for i in range(2, n):
		if so(i, n):
			rp_list.append(i)
	return len(rp_list)

max_idx = 0
max_pct = 0
for i in range(1, 10001):
	print(i)
	pct = i / rp(i)
	if pct > max_pct:
		max_pct = pct
		max_idx = i

print(max_idx, max_pct)
		
'''	
'''
'''
		
	
	
	factors = [1]
	i = 2
	while n != 1:
		if n % i == 0:
			if i not in factors:
				factors.append(i)
			n = int(n / i)
			continue
		i += 1
	factor_map[n] = factors
	return factors

def rp(n):
	n_factor = factor_list(n)
	rp_cnt = 1
	rp_list = {}
	for i in range(2, n):
		if i in rp_list:
			continue
		i_factor = factor_list(i)
		if len(n_factor) + len(i_factor) - 1 == len(set(n_factor + i_factor)):
			rp_cnt += 1
			k = 1
			while True:
				rp_list[k * i] = True
				if k * i > n:
					break
				k += 1
				
	return rp_cnt
	

max = 0
idx = 0
for i in range(2, 10001):
	print(i)
	phi = i / rp(i)
	if max < phi:
		idx = i
		max = phi

print(idx, max)
'''	
	
