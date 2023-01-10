# find LCM

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

d = 2
factor = 1
while True:
	if len(a) == 0:
		break
	is_divided = False
	for i, v in enumerate(a):
		if v % d == 0:
			is_divided = True
			a[i] = a[i] / d
	if is_divided:
		factor *= d
		a = [z for z in a if z != 1]
		continue
	else:
		d = d + 1

print(factor)
