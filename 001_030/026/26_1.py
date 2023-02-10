
def f_div(a):
	p = 1
	i = 1
	v_list = ""
	while True:
		i += 1
		if i == 100: break
		p = p * 10
		v = int(p / a)
		p = p % a
		v_list += str(v)
		if v_list == "0":
			v_list = ""
	return v_list
'''		
		list_len = len(v_list)
		for i, c in enumerate(v_list[:-1]):
			if str(v) == c:
				seg_len = list_len - i - 1
				if v_list[list_len - seg_len - seg_len:list_len - seg_len] == v_list[list_len - seg_len:list_len]:
					return seg_len, v_list[list_len - seg_len:list_len]
'''
print(f_div(101))
'''
max_length = 0
for i in range(1, 1000):
	v, s = f_div(i)
	print("%d - %d - %s" % (i, v, s))

	max_length = max(max_length, v)

print(max_length)
'''
			
