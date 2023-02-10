
def factorial(i):
	if i == 0:
		return 1
	elif i == 1:
		return 1
	else:
		return i * factorial(i - 1)

i = 3
while True:
	i_str = str(i)
	sum = 0
	for c in i_str:
		sum += factorial(int(c))
	if sum == i:
		print(i)
	i += 1
