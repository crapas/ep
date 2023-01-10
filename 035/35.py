import math
memo = {}
memo[0] = False
memo[1] = False
memo[2] = True

def is_prime(i):
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			memo[i] = False
			return False
	memo[i] = True
	return True

result = []

for i in range(1000000):
	if i in memo and memo[i] = False:
		continue:
	i_str = str(i)
	if i == 2:
		result.append(2)
		continue


	

