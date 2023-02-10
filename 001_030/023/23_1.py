import copy
d = []

def proper_divisors_sum_list(upper):
	divs = []
	for i in range(0, upper + 1):
		divs.append([1])
	
	for i in range(2, upper + 1):
		for j in range(2, int(i / 2) + 1):
			if i % j == 0:
				small = int(i / j)
				for v in divs[small]:
					if v not in divs[i]:
						divs[i].append(v)
					if v * j not in divs[i]:
						divs[i].append(v * j)
			
		
	return divs

q = proper_divisors_sum_list(30000)
for i in range(1, 30000):
	print(i, sorted(q[i]))

		
	
		
