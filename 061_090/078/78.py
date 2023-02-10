memo = {}

target = 1000


def use_one(target, small):
	if (target, small) in memo:
		return memo[(target, small)]
	if target == 0:
		return 1
	if target < 0:
		return 0
	sum = 0
	for c in range(1, small + 1):
#		if c > small:
#			break
		sum += use_one(target - c, c)	
	memo[(target, small)] = sum
	return sum
				
	
#for i in range(1000):
i = 1
while True:
	cnt = use_one(i, i)
	print(i, cnt)
	if cnt % 1000000 == 0:
		break
	i += 1
