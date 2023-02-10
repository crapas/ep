
def test(num_str):
	# 1234567890 -> 10 digit
	#d2d3d4 : num_str[1:4]
	if int(num_str[1:4]) % 2 != 0:
		return False
	if int(num_str[2:5]) % 3 != 0:
		return False
	if int(num_str[3:6]) % 5 != 0:
		return False
	if int(num_str[4:7]) % 7 != 0:
		return False
	if int(num_str[5:8]) % 11 != 0:
		return False
	if int(num_str[6:9]) % 13 != 0:
		return False
	if int(num_str[7:10]) % 17 != 0:
		return False
	return True


def make_pd(num_str, i):
	result = []
	temp_list = []
	for x in range(len(num_str)):
		temp_list.append(num_str[:x + 1] + str(i) + num_str[x + 1:])
	if i != 0:
		temp_list.append(str(i) + num_str)
	if i == 0:
		return temp_list
	else:
		for l in temp_list:
			result = result + make_pd(l, i - 1)
	return result

pd_list = make_pd("", 9)
sum = 0
for pd in pd_list:
	if test(pd):
		sum += int(pd)

print(sum)

