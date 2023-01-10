
i = 2
while True:
	a = str(i)
	b = [int(c) ** 5 for c in a]
	sum_v = sum(b)
	if i == sum_v:
		print("%d Match" % i)
	else:
		print(sum_v - i)
	i += 1


# largest - 443839
# single character ** 5's mac = 9 ** 5 = 59049
# so, n-digit sum : n * 59049
# n = 1 : 0~59049
# n = 2 : 0~118098
# n = 3 : 0~177147
# n = 4 : 
#... I don't know how I prove it.

