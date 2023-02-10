
prime = {}
prime[1] = False
prime[2] = True
def is_prime(n):
	if n in prime:
		return prime[n]
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			prime[n] = False
			return False
	prime[n] = True
	return True

def combination(n):
	pair = []
	if n < 10:
		return []
	str_n = str(n)
	length = len(str_n)
	for i in range(length - 1):
		p1 = str_n[:i + 1]
		p2 = str_n[i + 1:]
		if p1 == p2:
			continue
		if (int(p2), int(p1)) in pair:
			continue
		pair.append((int(p1), int(p2)))
	return pair

print(is_prime(1))
result_list = []
i = 1
while True:
#	print(i)
	p_l = combination(i)
	i += 2
	if len(p_l) < 5:
		continue
	pp_cnt = 0
	pp_pair = []
	for pair in p_l:
		if is_prime(int(pair[0])) and is_prime(int(pair[1])):
			pp_cnt += 1
			pp_pair.append(pair)
			if pp_cnt == 5:
				print("%d : add : " % i, pp_pair)
				result_list.append(pp_pair)

	if i > 10000000000:
		break
print(result_list)

			 
	

