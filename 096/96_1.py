
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

# (0,0) (1,0), (2,0), ..., (8, 0)
# (0,1), ...
# ...
# (0, 8), ..., (8, 8)

def print_game(game):
    for y in range(9):
        for x in range(9):
            print(game[y][x], end=" ")
        print()

def get_3_num(game):
    return game[0][0] * 100 + game[0][1] * 10 + game[0][2]

def check_cor(y, x):
    result = set()
    for i in range(9):
        if i != x:
            result.add((y, i))
        if i != y:
            result.add((i, x))
    x_grid = int(x / 3) * 3
    y_grid = int(y / 3) * 3
        
    x_pan = [x_grid + i for i in range(3)]
    y_pan = [y_grid + i for i in range(3)]
    #print(x_pan)
    #print(y_pan)
    for j in y_pan:
        for i in x_pan:
            if j != y and i != x:
                result.add((j, i))
    return(result)

def count0(game):
    cnt = 0
    for line in game:
        for value in line:
            if value == 0:
                cnt += 1
    return cnt
def possible_list(y, x, game):
    checks = check_cor(y, x)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for check in checks:
        y = check[0]
        x = check[1]
        value = game[y][x]
        if value != 0 and value in numbers:
            numbers.remove(value)
    return numbers

#print_game(games[0])
#print(get_3_num(games[0]))

game = games[49]
#print(check_cor(4, 7))
before = -1
while True:
    print_game(game)
    c0 = count0(game)
    print(c0)
    if c0 == before:
        break
    before = c0
    for y in range(9):
        for x in range(9):
            if game[y][x] == 0:
                possible = possible_list(y, x, game)
                print(len(possible))
                if len(possible) == 1:
                    game[y][x] = possible[0]
    
    poss_map = {}
    for y in range(9):
        for x in range(9):
            if game[y][x] == 0:
                poss_map[(y, x)] = possible_list(y, x, game)
    
    

