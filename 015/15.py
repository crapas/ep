
x = 20
y = 20

def cal_path(x, y):
	if x == 0:
		return 1
	if y == 0:
		return 1
	return cal_path(x - 1, y) + cal_path(x, y - 1) 

print(cal_path(x, y))
