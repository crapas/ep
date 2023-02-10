adj_cnt = 13

with open("number", "r") as wp:
	number_text = wp.read()

numbers = []
for c in number_text:
	if c.isdecimal():
		numbers.append(int(c))

given_count = len(numbers)
max_v = 0
for i in range(0, given_count - adj_cnt):
	pd = 1
	for j in range(0, adj_cnt):
		pd *= numbers[i + j]
	max_v = max(max_v, pd)

print(max_v)
