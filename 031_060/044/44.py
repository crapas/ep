import sys

pentagon_list = []

for i in range(1, 10000):
	pentagon_list.append(int(i * (3 * i - 1) / 2))

min_v = sys.maxsize

for i in range(1, 10000):
	print(i)
	for j in range(i + 1, 10000):
		pi = pentagon_list[i - 1]
		pj = pentagon_list[j - 1]
		if pi + pj in pentagon_list and pj - pi in pentagon_list:
			print(i, j)
			if pj - pi < min_v:
				print("== > ", i, j)
				min_v = pj - pi

print(min_v)
				
