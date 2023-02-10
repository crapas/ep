
seg_number = 4

number = []
with open("number", "r") as rf:
	while True:
		line = rf.readline()
		if not line:
			break
		number_split = line.strip().split(" ")
		number_in_line = []
		for number_str in number_split:
			number_in_line.append(int(number_str))
		number.append(number_in_line)

max = 0
		
# vertical
for i in range(20 - seg_number):
	for j in range(20):
		pd_value = number[i][j] * number[i + 1][j] * number[i + 2][j] * number[i + 3][j]
		if max < pd_value:
			max = pd_value

# horionzontal
for i in range(20):
	for j in range(20 - seg_number):
		pd_value = number[i][j] * number[i][j + 1] * number[i][j + 2] * number[i][j + 3]
		if max < pd_value:
			max = pd_value

# for diagonal down

for i in range(20 - seg_number):
	for j in range(20 - seg_number):
		pd_value = number[i][j] * number[i + 1][j + 1] * number[i + 2][j + 2] * number[i + 3][j + 3]
		if max < pd_value:
			max = pd_value

# for diagonal up
for i in range(20 - seg_number):
	for j in range(20 - seg_number):
		pd_value = number[i + seg_number][j] * number[i + seg_number - 1][j + 1] * number[i + seg_number - 2][j + 2] * number[i + seg_number - 3][j + 3]
		if max < pd_value:
			max = pd_value
print(max)
