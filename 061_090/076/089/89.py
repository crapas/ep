
def chain(n):
	while True:
		n_str = str(n)
		sum = 0
		for n_c in n_str:
			sum += int(n_c) ** 2
		n = sum
		if n == 1 or n == 89:
			return n

cnt = 0
for i in range(1, 10000000):
	if i % 100000 == 0:
		print(i / 100000)
	if chain(i) == 89:
		cnt += 1
print(cnt)
