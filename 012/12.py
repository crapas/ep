import math


def factor_number(i):
	factor_number = 0
	check_upper = int(math.sqrt(i))
	for j in range(check_upper):
		if i % (j + 1) == 0:
			factor_number += 2
	if math.sqrt(i) == int(math.sqrt(i)):
		factor_number -= 1
	return factor_number
			
'''
	factor = 2
	while True:
		if i % factor == 0:
			if len(factor_list) == 0:
				factor_list.append(factor)
			elif factor_list[-1] != factor:
				factor_list.append(factor)
			i /= factor
			continue
		factor += 1
		if i < factor:
			break
	return factor_list
'''

i = 1
sum = 0
while True:
	sum = sum + i
	fnum = factor_number(sum)
	if fnum > 500:
		print(sum)
		break
	print("%d : %d - %d" % (i, sum, fnum))
	i = i + 1
