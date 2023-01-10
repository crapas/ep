

f = []
f.append(1)
f.append(1)
while True:
	f.append(f[-1] + f[-2])
	if len(str(f[-1])) >= 1000:
		print(len(f))
		break
