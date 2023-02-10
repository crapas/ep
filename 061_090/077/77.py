memo = {}
def get_prime_list(n):
	check = []
	prime_list = []
	for i in range(0, n):
		check.append(True)
	check[0] = False		# 1
	for i in range(0, n):
		if check[i] == True:
			next_prime = i + 1
			prime_list.append(next_prime)
			primex = next_prime
			while primex <= n:
				check[primex - 1] = False
				primex += next_prime
	return prime_list



coin_list = get_prime_list(5000)
print(coin_list)


target = 1000


def use_one(target, small):
	if (target, small) in memo:
		return memo[(target, small)]
	if target == 0:
		return 1
	if target < 0:
		return 0
	sum = 0
	for c in coin_list:
		if c > small:
			break
		sum += use_one(target - c, c)	
	memo[(target, small)] = sum
	return sum
				
	

#print(use_one(target, 1000))
for i in range(100):
	print(i, use_one(i, i))
