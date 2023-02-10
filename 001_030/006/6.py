sum = 0
sum_sq = 0
upper = 100

for i in range(0, upper):
	sum += (i + 1)
	sum_sq += (i + 1) ** 2


print(sum ** 2 - sum_sq)

