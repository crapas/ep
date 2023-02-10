
def get_score(name):
	name_sum = 0
	for c in name:
		name_sum += ord(c) - ord('A') + 1
	return name_sum

	
names = []
with open("names.txt", "r") as fp:
	name_line = fp.read()
name_split = name_line.strip().split(",")
for n in name_split:
	names.append(n[1:-1])

names.sort()

sum = 0

for i, name in enumerate(names):
	score = get_score(name)
	sum += (i + 1) * score

	
print(sum)

