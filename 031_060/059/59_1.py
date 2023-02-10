from PyDictionary import PyDictionary
dictionary = PyDictionary()
code_list = []
with open("cipher.txt", "r") as rp:
	code_list = rp.read().strip().split(",")


pwd_list = []
for a in range(ord('a'), ord('z') + 1):
	for b in range(ord('a'), ord('z') + 1):
		for c in range(ord('a'), ord('z') + 1):
			pwd_list.append((a, b, c))


test = False

max_word_cnt = 0
max_result = ""
max_pwd = ""
i = 0
for pwd in pwd_list:
	total_word = 0
	word_in_dict = 0
	result = ""
	idx = 0

	for code in code_list:
		result += chr(int(code) ^ pwd[idx])
	words = result.split(" ")
	total_word = len(words)
#	for word in words:
#		print(word)
#		if dictionary.meaning(word):
#			word_in_dict += 1
#			print("word in dict")
			

		
	idx += 1
	if idx % 3 == 0:
		idx = 0	
#	print(result)
#	print(total_word)
#	print(word_in_dict)
#	print(word_in_dict / total_word)

	print(result)

	if max_word_cnt < total_word:
		max_word_cnt = total_word
		max_pwd = pwd
		max_result = result
#		print(max_pwd)
#		print(max_result)
#		print(max_word_cnt, len(result))
	
	if test:
		break

	
