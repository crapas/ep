
d = []

for i in range(10001):
	d.append(0)
for i in range(1, 10001):
	for j in range(1, i):
		if i % j == 0:
			d[i] += j

sum = 0
for i in range(1, 10001):
	v = d[i]
#	print(i, v)
	if v <= 10000 and d[v] == i and i != v:
		print(i, v)
		sum += i + v

print(sum / 2)
	
