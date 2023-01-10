
fac = 1
for i in range(0, 100):
	fac *= (i + 1)

fac_str = str(fac)
sum = 0
for v in fac_str:
	sum += int(v)

print(sum)	
