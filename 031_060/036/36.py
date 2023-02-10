import time

def change_dec(n):
	n_2 = ""
	while n > 1:
		n_2 = str(n % 2) + n_2
		n = int(n / 2)
	return "1" + n_2

	
def change_dec_to_bin_2(n):
	n_2 = ""
	while n > 1:
		n_2 = str(n & 1) + n_2
		n = n >> 1
	return "1" + n_2

s1 = time.time()
for i in range(200):
	change_dec(i)	
c1 = time.time()
for i in range(200):
	change_dec_to_bin_2(i)
c2 = time.time()

print(c1 - s1)
print(c2 - c1)
