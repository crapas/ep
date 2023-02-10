cnt = 0
i = 1
while True:
	print("%dth" % i)
	j = 1
	while True:
		power = j ** i
		power_len = len(str(power))
		if power_len == i:
			print("%d = %d ^ %d" % (power, j, i))
			cnt += 1
		if power >= 10 ** i:
			break
		j += 1
	i += 1
	if i == 30:
		break

print(cnt)

