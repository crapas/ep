def test(n):
	num_str = []
	for i in range(6):
		num_str.append([])
		temp_str = str(n * (i + 1))
		for c in temp_str:
			num_str[i].append(c)
		num_str[i].sort()
	for i in range(5):
		if num_str[i] != num_str[i + 1]:
			return False
	return True
#	if len(num_str[0]) != len(num_str[5]):
#		return False
#	if sorted(
	print(num_str)
'''		
		num_str.append(str(n * (i + 1)))
	if len(num_str[0]) != len(num_str[5]):
		return False
	num_str_arr = []
	for 
	num1_str = str(n)
	num6_str = str(n * 6)
	if len(num1_str) != len(num6_str):
		return False
	num2_str = str
'''

i = 1
while True:
	if test(i):
		print(i)
		break
	i += 1
