#upper = 200000000
upper = 30
check = [True]
prime = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(upper * 2):
    check.append(True)
    if i % 2 == 0:
        check[i] = False
    elif i % 3 == 0:
        check[i] = False
    elif i % 5 == 0:
        check[i] == False
    elif i % 7 == 0:
        check[i] == False
    elif i % 11 == 0:
        check[i] == False
    elif i % 13 == 0:
        check[i] = False
    elif i % 17 == 0:
        check[i] = False
    elif i % 19 == 0:
        check[i] = False

print("Process A Ready")
check[0] = False
check[1] = False

for i in range(20, upper * 2):
    if not check[i]:
        continue
    prime.append(i)
    remove = i
    while True:
        if remove >= upper:
            break
        check[remove] = False
        remove += i
#        print(remove)
        

#print(prime[0:100])
#print(len(prime))
print("Ready for prime list")
sum = 0
for i in range(1, upper + 1):
    div_list = []
    test = 1
    while True:
        if i % test == 0:
            if i // test == test:
                div_list.append(test)
                break
            elif i // test > test:
                break
            else:
                div_list.append(test)
                div_list.append(i // test)
        test += 1
    pgi = True
    for div in div_list:
        if div + i // div not in prime:
            pgi = False
            break
    if pgi:
        print("ADD : ", i)
        sum += i
print(sum)