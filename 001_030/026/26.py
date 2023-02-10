
def f_div(a):
	p = 1
	i = 1
	v_list = []
	while True:
		p = p * 10
		v = int(p / a)
		p = p % a
		if p == 0:
			return 0
		v_list.append(v)
		list_len = len(v_list)
		if list_len % 2 == 0:
			if v_list[0:int(list_len / 2)]  == v_list[int(list_len / 2):]:
				return list_len / 2

print(f_div(6))
max_length = 0
for i in range(1, 1000):
	print(i)
	max_length = max(max_length, f_div(i))

print(max_length)
			
