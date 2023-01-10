import sys

sys.setrecursionlimit(3000)

memo = {}
memo[1] = 1

def find_chain_length(i):
	if i in memo:
		return memo[i]
	else:
		if i % 2 == 0:
			memo[i] = 1 + find_chain_length(int(i / 2))
		else:
			memo[i] = 1 + find_chain_length(i * 3 + 1)
	return memo[i]
		

upper = 1000000
max_chain = -1
max_index = -1
for i in range(1, upper):
	chain_length = find_chain_length(i)
	if max_chain < chain_length:
		max_chain = chain_length
		max_index = i
			

print(max_index, max_chain)
