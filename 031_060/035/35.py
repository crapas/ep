import math
memo = {}
memo[0] = False
memo[1] = False
memo[2] = True

def get_rotation_and_check2(n):
	result = []
	n_str = str(n)
	if '2' in n_str:
		return [-1]
	for i in range(1, len(n_str)):
		result.append(int(n_str[i:] + n_str[:i]))
	return result

def is_prime(i):
	for j in range(2, int(math.sqrt(i)) + 1):
		if i % j == 0:
			memo[i] = False
			return False
	memo[i] = True
	return True

#print(get_rotation(12345))

result = [2]

for i in range(3, 1000000):
	if not is_prime(i):
		continue
	rots = get_rotation_and_check2(i)
	if rots == [-1]:
		continue
	check = True
	for rot in rots:
		if not is_prime(rot):
			check = False
			break
	if check:
		result.append(i)
	print(i)

print(len(result))
	

