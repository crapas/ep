
def add_one(numbers):
	check = []
	new_numbers_list = []
	for i in range(0, 10):
		check.append(False)
	for number in numbers:
		check[int(number)] = True
	for i in range(1, 10):
		if check[i] == False:
			new_numbers_list.append(numbers + str(i))

	if len(numbers) == 8:
		return new_numbers_list
	else:
		return_numbers = []
		for new_number in new_numbers_list:
			return_numbers += add_one(new_number)
		return return_numbers


returned = add_one("")
result = set()
for r in returned:
	#case 1 : 1 * 4 = 4
		a = int(r[0])
		b = int(r[1:5])
		c = int(r[5:9])
		if c == a * b:
			result.add(c)
			continue

	#case 2 : 2 * 3 = 4
		a = int(r[0:2])
		b = int(r[2:5])
		c = int(r[5:9])
		if c == a * b:
			result.add(c)
			continue
		

	#case 3 : 3 * 2 = 4
		a = int(r[0:3])
		b = int(r[3:5])
		c = int(r[5:9])
		if c == a * b:
			result.add(c)
			continue

	#case 4 : 4 * 1 = 4
		a = int(r[0:4])
		b = int(r[4:5])
		c = int(r[5:9])
		if c == a * b:
			result.add(c)
			continue

print(result)
print(sum(result))
		
		
