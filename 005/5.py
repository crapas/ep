upper = 20

result = 1

while True:
	check = 0
	for i in range(upper):
		check += result % (i + 1)
	if check == 0:
		break
	result += 1

print(result)

