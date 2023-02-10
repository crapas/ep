def getPenta(k):
# n: 1, -1, 2, -2, 3, -3 ...
	n = (k/2 + 1 if k % 2 == 0 else (k / 2)* -1 - 1)
	return int(n*(3*n - 1) / 2)

signs = (1, 1, -1, -1)
p = [1]
k = 1
while True:
	pk = 0
	i = 0
	penta = getPenta(i)
	while penta <= k:
		pk += signs[i%4] * p[k-penta]
		i += 1
		penta = getPenta(i)
	print(pk)
	pk = pk % 1000000
	if pk == 0:
		print(k)
		break
	p.append(pk)
	print(k)
	k += 1
