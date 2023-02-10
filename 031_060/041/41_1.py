import math

memo = {}
def is_prime(n):
	if n in memo:
		return memo[n]
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			memo[n] = False
			return False
	memo[n] = True
	return True

def is_pandigital(n):
	n_str = str(n)
	if '0' in n_str:
		return False

	str_len = len(n_str)
	for i in range(str_len):
		if len(n_str) == 0:
			return False
		if str(i + 1) not in n_str:
			return False
		n_str = n_str.replace(str(i + 1), "")
	return True

def add_1_character(given_list, c):
	new_list = []
	if given_list == []:
		return(["1"])
	for l in given_list:
		length = len(l)
		for i in range(length):
			new_str = l[0:i] + c + l[i:]
			new_list.append(new_str)
		new_list.append(l + c)
	return new_list


#print(is_prime(2143))
#print(is_pandigital(2143))

pp_list = []
step_list = []
for i in range(1, 10):
	step_list = add_1_character(step_list, str(i))
	for s in step_list:
		if is_prime(int(s)):
			pp_list.append(int(s))
			print(s)

print(max(pp_list))
#for i in range(2, 987654322):
#	if is_prime(i) and is_pandigital(i):
#		print(i)

