import math
memo = {}

a_lower = -999
a_upper = 999
b_lower = -1000
b_upper = 1000

def is_prime(a):
	if a in memo:
		return memo[a]
	for i in range(2, int(math.sqrt(a)) + 1):
		if a % i == 0:
			memo[a] = False
			return False
	memo[a] = True
	return True

max = -1
m_a = -1
m_b = -1
for a in range(a_lower, a_upper + 1):
	for b in range(b_lower, b_upper + 1):
		n = 0
		while True:
			v = n ** 2 + a * n + b
			if v < 0:
				break
			if not is_prime(v):
				break
			n += 1
#		print("%d - %d : %d" %( a, b, n))
		if max < n:
			max = n
			m_a = a
			m_b = b

print(m_a, m_b, max, m_a * m_b)
			
