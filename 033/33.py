fracs = []
for i in range(10, 100):
	for j in range(i + 1, 100):
		a1 = int(i / 10)
		a2 = i % 10
		b1 = int(j / 10)
		b2 = j % 10
		div_v = i / j
		if a1 == b1 and b2 != 0 and a2 / b2 == div_v:
			fracs.append((a2, b2))
		elif a1 == b2 and b1 != 0 and a2 / b1 == div_v:
			fracs.append((a2, b1))
		elif a2 == b1 and b2 != 0 and a1 / b2 == div_v:
			fracs.append((a1, b2))
#		elif a2 == b2 and b1 != 0 and a1 / b1 == div_v:
#			fracs.append((i, j))

up = 1
down = 1
for tup in fracs:
	up *= tup[0]
	down *= tup[1]

print(up, down)

i = 2
target = up
while True:
	if up % i == 0 and down % i == 0:
		up /= i
		down /= i
	else:
		i = i + 1
	if i == target or up == 1:
		print(down)
		break
	
