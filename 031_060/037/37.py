import math

memo = {}
memo[0] = False
memo[1] = False
def check_prime(n):
	if n in memo:
		return memo[n]
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			memo[n] = False
			return False
	memo[n] = True
	return True

tp_cnt = 0
i = 10
tp_list = []
while True:
	test = str(i)
	not_prime = False
	while len(test) > 0:
		if not check_prime(int(test)):
			not_prime = True
		test = test[1:]
	test = str(i)
	while len(test) > 0:
		if not check_prime(int(test)):
			not_prime = True
		test = test[:-1]

	if not not_prime:
		tp_list.append(i)
		print(i)
	if len(tp_list) == 11:
		break
	i = i + 1

print(sum(tp_list))
		
