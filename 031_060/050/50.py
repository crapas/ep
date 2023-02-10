upper = 1000000
#upper = 1000
def find_prime_until(n):
	prime_list = []
	number_list = []
	number_list.append(False)
	number_list.append(False)
	for i in range(2, n + 1):
		number_list.append(True)

	prime = 0
	while True in number_list:
#		check = prime
		while True:
			if number_list[prime] == True:
				break
			prime += 1
		prime_list.append(prime)
#		print(prime)
		i = 1
		while True:
			if i * prime > n:
				break
			number_list[i * prime] = False
			i += 1
	return prime_list

#print(find_prime_until(100))
prime_list = find_prime_until(upper + 10)
print("Complete")
#prime_list = find_prime_until(200000022)
#print(find_prime_until(2000000))
i = 0
max_sum = 0
max_seq = 0
result = 0
while True:
	print("==> %d" % i)
#	if prime_list[i] > 1000000:
	if prime_list[i] > upper:
		break
	seq = 1
	this_max = 0
	this_result = 0
	p_sum = prime_list[i]
	while True:
		add_prime = prime_list[i + seq]
		print(add_prime)
		if add_prime > upper:
			break
		p_sum += add_prime
		if p_sum > upper:
			break
		if p_sum > max_sum:
			max_sum = p_sum
#			print(max_sum)
		if p_sum in prime_list:
#			print(p_sum, prime_list[i], seq + 1)
#			print("Check")
			if this_max < (seq + 1):
				this_max = seq + 1
				this_result = p_sum
		seq += 1
	if max_seq < this_max:
		max_seq = this_max
		result = this_result
	
	i += 1
print(max_sum)
print(max_seq)
print(result)
			
		
		
	

