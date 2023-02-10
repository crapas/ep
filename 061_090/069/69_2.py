def so(a, b):
	if a > b: 
		x = a % b
		y = b
	else:
		x = b % a
		y = a
	while x != 0:
		temp = x
		x = y % x
		y = temp
#		print(y, x)

	if y == 1:
		return True
	else:
		return False


def rp(n):
	rp_list = [1]
	for i in range(2, n):
		if so(i, n):
			rp_list.append(i)
	return len(rp_list)


max_idx = 0
max_pct = 0
for i in range(1, 1000001):
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
	
