import time

def change_dec_to_bin_2(n):
	n_2 = ""
	while n > 1:
		n_2 = str(n & 1) + n_2
		n = n >> 1
	return "1" + n_2

def check_palindromic(i):
	if i == i[::-1]:
		return True


db_p_list = []
for i in range(1, 1000000):
	dec_str = str(i)
	bin_str = change_dec_to_bin_2(i)

	if check_palindromic(dec_str) and check_palindromic(bin_str):
		db_p_list.append(i)


print(sum(db_p_list))
