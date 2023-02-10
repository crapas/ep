
coin_list = [200, 100, 50, 20, 10, 5, 2, 1]

target = 200

def use_one(target, last):
	sum = 0
	for coin in coin_list:
		if coin <= last:
			if target - coin > 0:
				sum = sum + use_one(target - coin, coin)
			elif target == coin:
				sum = sum + 1
	return sum

print(use_one(target, 1000))
			
