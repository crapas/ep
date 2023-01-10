
def find_chain_length(i):
	chain = 0
	while True:
		chain += 1
		if i == 1:
			break
		if i % 2 == 0:
			i = i / 2
		else:
			i = i * 3 + 1
	return chain

upper = 1000000
max_chain = -1
max_index = -1
for i in range(1, upper):
	chain_length = find_chain_length(i)
	if max_chain < chain_length:
		max_chain = chain_length
		max_index = i
			

print(max_index, max_chain)
