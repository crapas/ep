
tr_t = 285
tr_p = 165
tr_h = 143
t = 40755
p = 40755
h = 40755
'''
tr_t = 1
tr_p = 1
tr_h = 1
t = 1
p = 1
h = 1
'''

while True:
	h = 4 * tr_h + 1 + h
	tr_h += 1
	while True:
		p = 3 * tr_p + 1 + p
		tr_p += 1
		if p >= h:
			break
	while True:
		t = tr_t + 1 + t
		tr_t += 1
		if t >= h:
			break
	print(tr_t, tr_p, tr_h, t, p, h)
	if t == p and p == h:
		print(t)
		break



