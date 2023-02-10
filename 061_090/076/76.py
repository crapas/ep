coin_list = []
for i in range(1, 100):
	coin_list.append(i)

target = 100

def use_one(target, last):
	sum = 0
	for coin in coin_list:
		if coin <= last:
			if target - coin > 0:
				sum = sum + use_one(target - coin, coin)
			elif target == coin:
				sum = sum + 1
			print(target)
	return sum

print(use_one(target, 1000))
			
