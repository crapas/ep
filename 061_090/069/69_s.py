def prime_list(n):
	prime = []
	i = 2
	while True:
		if n % i == 0:
			prime.append(i)
		i += 1
		if i == n:
			break
	return prime

p = prime_list(1000)
i = 0

f = 1
for pr in p:
	print(pr)

#print(f)
#print(i - 2)
