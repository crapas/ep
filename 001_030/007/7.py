
cnt = 0
i = 2

prime = []
while True:
	div_cnt = 0
	for j in range(1, i + 1):
		if i % j == 0:
			div_cnt += 1
	if div_cnt == 2:
		prime.append(i)
	if len(prime) == 500:
		break
	i += 1

print(prime[-1])

