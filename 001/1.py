
n = 1000
sum = 0
for i in range(0, n):
	if i % 3 == 0:
		sum += i
	if i % 5 == 0:
		sum += i
	if i % 15 == 0:
		sum -= i

print(sum)
