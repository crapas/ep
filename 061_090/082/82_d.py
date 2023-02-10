import sys
import copy
sys.setrecursionlimit(10000)
#memo = []
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
		numbers.append(segment)


def cost_to(x, y):
	return int(numbers[x][y])

def key_str(x, y):
	return "%d_%d" % (x, y)
width = len(numbers[0])
height = len(numbers)

def update_list(key):
	x_str, y_str = key.split("_")
	x = int(x_str)
	y = int(y_str)
	result = []
	if x != 0:
		result.append((x - 1, y))
	if y != 0:
		result.append((x, y - 1))
	if x != width - 1:
		result.append((x + 1, y))
	if y != height - 1:
		result.append((x, y + 1))
	return result

visit = {}
cost = {}

def next_visit():
	unvisited_key = []
	for k, v in visit.items():
		if v == False:
			unvisited_key.append(k)
	min_v = sys.maxsize
	min_idx = ""
	for unvisited in unvisited_key:
		if cost[unvisited] <= min_v:
			min_idx = unvisited
			min_v = cost[unvisited]
	return min_idx

for x in range(width):
	for y in range(height):
		key = key_str(x, y)
		visit[key] = False
		cost[key] = sys.maxsize

# 시작점 : 0_0

key = key_str(0, 0)
cost[key] = 0
while False in visit.values():
	current_key = next_visit()
	updates = update_list(current_key)
	visit[current_key] = True
	for update in updates:
		x = update[0]
		y = update[1]
		update_key = key_str(x, y)
		if cost[current_key] + cost_to(x, y) < cost[update_key]:
			cost[update_key] = cost[current_key] + cost_to(x, y)

target_key = key_str(width - 1, height - 1)
total_cost = cost[target_key] + cost_to(0, 0)
print(total_cost)


