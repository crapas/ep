
def f_div(a):
	p = 1
	i = 1
	v_list = ""
	while True:
		i += 1
		if i == 10000: break
		p = p * 10
		v = int(p / a)
		p = p % a
		if v == 0 and p == 0:
			return 0, "", ""
		v_list += str(v)
		if v_list == "0":
			v_list = ""

	# 1. cutting starting tresh
	list_len = len(v_list)
	possible_seg = ""
	for i, c in enumerate(v_list[:-1]):
		if str(v) == c:
			seg_len = list_len - i - 1
			if v_list[list_len - 2 * seg_len:list_len - seg_len] == v_list[list_len - seg_len:list_len]:
#				print(list_len, seg_len)
				possible_seg = v_list[list_len - seg_len:list_len]
				break
#	print("v, ", v_list)
#	print("p, ", possible_seg)	
	# 2. find pattern
	possible_len = len(possible_seg)
	for i in range(1, int(possible_len / 2) + 1):
		if possible_len % i == 0:
			rec_seg = possible_seg[0:i] * int(possible_len / i)
#			print(possible_seg[0:i])
#			print(possible_seg[-i:])
#			print(rec_seg)
#			print(possible_seg)
			if possible_seg == rec_seg:
#			if possible_seg[0:i] == possible_seg[-i:]:
#				print("match")
				return i, v_list, possible_seg[0:i]
#				break

	print("... %d [%s]" % (a, v_list))	
	
'''		
		list_len = len(v_list)
		for i, c in enumerate(v_list[:-1]):
			if str(v) == c:
				seg_len = list_len - i - 1
				if v_list[list_len - seg_len - seg_len:list_len - seg_len] == v_list[list_len - seg_len:list_len]:
					return seg_len, v_list[list_len - seg_len:list_len]
'''
max_length = 0
for i in range(1, 1000):
	v, l, s = f_div(i)
	print("%d - %d \n[%s]\n[%s]" %(i, v, l, s))
	max_length = max(max_length, v)

print(max_length)
			
