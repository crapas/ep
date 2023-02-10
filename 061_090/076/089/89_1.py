
#p(100) = sigma(1 ~ 99) p(n)

#p(1) = 1



def ways(n):
	if n == 1:
		return 1
	else:
		sum = 0
		for i in range(1, n):
			sum += ways(i)
		return sum

print(ways(5))
		
