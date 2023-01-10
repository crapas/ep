products = []

def check_palindrome(a):
	a_str = str(a)
	return a_str == a_str[::-1]
	# [a:b:c] means... from idx a, to indx b - 1, step c so ::-1 means everthing with reverse order


for i in range(100, 1000):
	for j in range(100, 1000):
		products.append(i * j)

products.sort(reverse = True)

for number in products:
	if check_palindrome(number):
		print(number)
		break

