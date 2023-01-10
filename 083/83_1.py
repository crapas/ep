import sys
import copy
sys.setrecursionlimit(10000)
memo = []
numbers = []
with open("number", "r") as rp:
	while True:
		line = rp.readline()
		if not line: break
		segment = line.strip().split(",")
		seg_len = len(segment)
		temp = []
		for i in range(seg_len):
			temp.append(-1)
		memo.append(temp)
		numbers.append(segment)


width = len(numbers[0])
height = len(numbers)


def find_2way_min(x, y):
	if memo[x][y] != -1:
		return memo[x][y]
	if x == 0 and y == 0:
		return int(numbers[0][0])
	temp = []
	if x != 0:
		temp.append(find_2way_min(x - 1, y))
	if y != 0:
		temp.append(find_2way_min(x, y - 1))

	memo[x][y] = int(numbers[x][y]) + min(temp)
	return memo[x][y]	
v1 = find_2way_min(height - 1, width - 1)
print(v1)

'''
def find_min(x, y, visit_list):
	visit_list.append((x, y))
	temp = []

	if x == 0 and y == 0:
		return int(numbers[0][0])
	if x != 0 and (x - 1, y) not in visit_list:
		temp.append(find_min(x - 1, y, copy.deepcopy(visit_list)))
	if y != 0 and (x, y - 1) not in visit_list:
		temp.append(find_min(x, y - 1, copy.deepcopy(visit_list)))

	if x != width - 1 and (x + 1, y) not in visit_list:
		temp.append(find_min(x + 1, y, copy.deepcopy(visit_list)))

	if y != height - 1 and (x, y + 1) not in visit_list:
		temp.append(find_min(x, y + 1, copy.deepcopy(visit_list)))

	while None in temp:
		temp.remove(None)	
	
	if len(temp) == 0:
		return None
	if min(temp) > v1:
		return None
	return_v = int(numbers[y][x]) + min(temp)
		
	print(len(visit_list), return_v)
	return return_v
'''

def find_min(x, y, total, visit_list):
	total += int(numbers[y][x])
	if total > v1:
#		print("Cut 1")
		return None
	if x == width - 1 and y == height - 1:
		print("Reach here")
		print(total)
		print(visit_list)
		return total
	visit_list.append((x, y))
	print(len(visit_list))
	temp = []
	if x != 0 and (x - 1, y) not in visit_list:
		temp.append(find_min(x - 1, y, total, copy.deepcopy(visit_list)))
	if y != 0 and (x, y - 1) not in visit_list:
		temp.append(find_min(x, y - 1, total, copy.deepcopy(visit_list)))
	if x != width - 1 and (x + 1, y) not in visit_list:
		temp.append(find_min(x + 1, y, total, copy.deepcopy(visit_list)))
	if y != height - 1 and (x, y + 1) not in visit_list:
		temp.append(find_min(x, y + 1, total, copy.deepcopy(visit_list)))
	while None in temp:
		temp.remove(None)
	if len(temp) == 0:
#		visit_list.remove((x, y))
		return None
	return min(temp)


	
		
	
#v = find_min(height - 1, width - 1, [])
v = find_min(0, 0, 0, [])

print(v1)
print(v)

