
# SF : 8
# 4C : 7
# FH : 6
# FL : 5
# SR : 4
# 3C : 3
# 2P : 2
# 1P : 1
# OTHERS : 0
def number_value(numbers):
	sorted_numbers = sorted(numbers)
	
	min_v = sorted_numbers[0]
	max_v = sorted_numbers[4]
	if [n - min_v for n in sorted_numbers] == [0, 1, 2, 3, 4]:
		return 4, max_v, max_v
	step = 0
	current = -1
	num_str = ""
	for i in range(5):
		if sorted_numbers[i] != current:
			current = sorted_numbers[i]
			step += 1
		num_str += str(step)
	if num_str == "11112":
		return 7, min_v, max_v
	if num_str == "12222":
		return 7, max_v, max_v
	if num_str == "11122":
		return 6, min_v, max_v
	if num_str == "11222":
		return 6, max_v, max_v
	if num_str == "11123":
		return 3, min_v, max_v
	if num_str == "12223":
		return 3, sorted_numbers[1], max_v
	if num_str == "12333":
		return 3, max_v, max_v
	if num_str == "12233" or num_str == "11233":
		return 2, max_v, max_v
	if num_str == "11223":
		return 2, sorted_numbers[3], max_v
	if num_str == "11234" or num_str == "12234":
		return 1, sorted_numbers[1], max_v
	if num_str == "12334" or num_str == "12344":
		return 1, sorted_numbers[3], max_v
	return 0, max_v, max_v
	

def is_flush(suit):
	shape = suit[0]
	for s in suit:
		if shape != s:
			return False
	return True

		
games = []
	
with open("poker.txt", "r") as rp:
	while True:
		line = rp.readline()
		if not line: break
		games.append(line.strip())

sum = 0
for game in games:
	winner = 1
	hands = game.split(" ")
	p1_hands = hands[0:5]
	p2_hands = hands[5:10]
	numbers = []
	suits = []
	for hand in hands:
		if hand[0] == 'A':
			numbers.append(14)
		elif hand[0] == 'K':
			numbers.append(13)
		elif hand[0] == 'Q':
			numbers.append(12)
		elif hand[0] == 'J':
			numbers.append(11)
		elif hand[0] == 'T':
			numbers.append(10)
		else:
			numbers.append(int(hand[0]))
		suits.append(hand[1])

	v1, n1, m1 = number_value(numbers[0:5])
	v2, n2, m2 = number_value(numbers[5:10])
	if_1 = is_flush(suits[0:5])
	if_2 = is_flush(suits[5:10])
	if if_1:
		if v1 == 4:
			v1 = 8
		else:
			v1 = 5
	if if_2:
		if v2 == 4:
			v2 = 8
		else:
			v2 = 5
#	print(numbers[0:5], suits[0:5])
#	print(v1, n1, m1)
#	print(if_1)
	if v1 > v2:
		winner = 1
	elif v1 < v2:
		winner = 2
	elif n1 > n2:
		winner = 1
	elif n1 < n2 :
		winner = 2
	elif m1 > m2 :
		winner = 1
	elif m1 < m2:
		winner = 2
	else:
		print("DRAW")
	if winner == 1:
		sum += 1

print(sum)
