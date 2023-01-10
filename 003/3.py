
#i = 600851475143
i = 906609

current_factor = 2
last_factor = -1
factor_list = []
while True:
	if i == 1:
		break
	if i % current_factor == 0:
		if last_factor != current_factor:
			last_factor = current_factor
			factor_list.append(current_factor)
		i = i / current_factor
	else:
		current_factor += 1

print(i)
print(factor_list)
	
