
def add_one(numbers):
	check = []
	new_numbers_list = []
	for i in range(10):
		check.append(False)
	for number in numbers:
		check[int(number)] = True
	for i in range(10):
		if check[i] == False:
			new_numbers_list.append(numbers + str(i))

	if len(numbers) == 9:
		return new_numbers_list
	else:
		return_numbers = []
		for new_number in new_numbers_list:
			return_numbers += add_one(new_number)
		return return_numbers


r = add_one("")
print(r[999999])
		
		
