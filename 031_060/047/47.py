import math

prime = [2]
pf_map = [False, False, False, False]
def is_prime(n):
	if n in prime:
		return True
	
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	
	prime.append(n)
	return True

def decomposition(s):
	factor_list = []
	n = s
	i = 2
	while True:
		if i == s:
			break
		if n % i == 0:
			n = int(n / i)
			if i not in factor_list:
				factor_list.append(i)
				if len(factor_list) == 5:
					return False
			continue
		i += 1
	if len(factor_list) == 4:
		return True
	return False

c = 4
while True:
	if decomposition(c):
		print("%d - True" % c)
		pf_map[c % 4] = True
	else:
		pf_map[c % 4] = False
		print("%d - Not True" % c)
	if False not in pf_map:
		print(c - 3)
		break
	c = c + 1
	
