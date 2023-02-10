t_list = []
memo = {}

def conv_word_to_number(word):
	sum = 0
	for char in word:
		sum += ord(char) - ord('A') + 1
	return sum

def t_n(n):
	if n in memo:
		return memo[n]
	i = 1
	t = 0
	while True:
		t += i
		if t == n:
			memo[n] = True
			return True
		if t > n:
			memo[n] = False
			return False
		i += 1
	
with open("words.txt", "r") as rp:
	input_text = rp.read()

words = input_text.strip().split(",")
cnt = 0
for word in words:
	word_num = conv_word_to_number(word[1:-1])
	if t_n(word_num):
		cnt += 1

print(cnt)
