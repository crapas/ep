rec = []
size = 1001
num = size * size

x = int(size / 2)
y = int(size / 2)

for i in range(size):
	rec.append([])
	for j in range(size):
		rec[i].append(0)

dir = 1		# 1 right 2 down 3 left 4 up
step_cnt = 0
change_direction_cnt = 0
step = 1

c_cnt = 0
for i in range(num):
	rec[x][y] = i + 1
	if dir == 1:
		x += 1
	if dir == 2:
		y += 1
	if dir == 3:
		x -= 1
	if dir == 4:
		y -= 1

	step_cnt += 1
	if step_cnt == step:
		dir += 1
		step_cnt = 0
		if dir == 5:
			dir = 1
		change_direction_cnt += 1
		if change_direction_cnt == 2:
			change_direction_cnt = 0
			step += 1
		
sum = 0

for i in range(size):
	sum += rec[i][i]
	sum += rec[i][size - i - 1]
sum -= 1

print(sum)
	
	
	

