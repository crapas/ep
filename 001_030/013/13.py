
import math

sum = 0

with open("number", "r") as rp:
	while True:
		line = rp.readline()
		if not line:
			break
		sum += int(line.strip())

ciper = int(math.log(sum, 10))
result = int(sum / (10 ** (ciper - 9)))

print(result)
