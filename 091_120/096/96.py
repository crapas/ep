def count0(game):
	cnt = 0
	for x in range(9):
		for y in range(9):
			if game[x][y] == 0:
				cnt += 1
	return cnt

def check_cor(x, y):
	cor = set()
	for i in range(9):
		if i != x:
			cor.add((i, y))
		if i != y:
			cor.add((x, i))
	x_pan = [int(x / 3) * 3, int(x / 3) * 3 + 1, int(x / 3) * 3 + 2]
	y_pan = [int(y / 3) * 3, int(y / 3) * 3 + 1, int(y / 3) * 3 + 2]

	for i in x_pan:
		for j in y_pan:
			if i != x and j != y:
#			if (i, j) != (x, y):
				cor.add((i, j))
	return cor
	
def possible(x, y, game):
	number = [True for _ in range(9)]
	checks = check_cor(x, y)
	for check in checks:
		number[game[check[0]][check[1]] - 1] = False
	result = []
#	print(number)
	for i in range(9):
		if number[i] == True:
			result.append(i + 1)
	return result

		
games = []
with open("sudoku.txt", "r") as rp:
	for i in range(50):
		rp.readline()
		a_game = []
		for j in range(9):
			a_list = []
			line = rp.readline().strip()
			for c in line:
				a_list.append(int(c))
			a_game.append(a_list)
		games.append(a_game)

print(games[1])			

sum = 0
for i in range(50):
	game = games[i]
	c0 = -1
	possible_map = {}
	while True:
		for x in range(9):
			for y in range(9):
				print(game[x][y], end=" ")
			print()
		before_c0 = c0
		c0 = count0(game)
		print("0 Cnt", c0)
		if c0 == 0:
			break
		if c0 == before_c0:
			break
		possible_map = {}
		for x in range(9):
			for y in range(9):
				if game[x][y] == 0:
					possible_v = possible(x, y, game)
					print(x, y, possible_v)
					possible_map[(x, y)] = possible_v
#					possible_map[(x, y)] = possible(x, y, game)
#		print("Possible Map :", possible_map)
		for k, v in possible_map.items():
			if len(v) == 1:
				game[k[0]][k[1]] = v[0]
#	c0 = count0(game)
#	print("0 Cnt", c0)
			
	
	print(possible_map)
	break


		
