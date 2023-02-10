factor_map = {}
factor_map[1] = [1]
factor_map[2] = [1, 2]
def factor_list(n):
	if n in factor_map:
		return factor_map[n]
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
	rp_cnt = 0
	for i in range(1, n):
		i_factor = factor_list(i)
		if len(n_factor) + len(i_factor) - 1 == len(set(n_factor + i_factor)):
			rp_cnt += 1
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
	
	
