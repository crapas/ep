
max = 4000000
fib = []
fib.append(1)
fib.append(2)

while True:
	fib.append(fib[-1] + fib[-2])
	if fib[-1] >= 4000000:
		break

fib_length = len(fib) - 1

sum = 0
for i in range(0, fib_length):
	if fib[i] % 2 == 0:
		sum += fib[i]

print(sum)
