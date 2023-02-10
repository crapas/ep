#upper = 200000000
upper = 100000000
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

print("Init Done")

check[0] = False
check[1] = False

for i in range(20, upper * 2):
    if not check[i]:
        continue
    prime.append(i)
    remove = i
    while True:
        if remove >= upper * 2:
            break
        check[remove] = False
        remove += i
#        print(remove)
        

print("Prime List Ready")
#print(prime)
sum = 0
for i in range(1, upper + 1):
    div_list = []
    test = 1
    while True:
        if i % test == 0:
#            print(i // test, test)
            if i // test == test:
                div_list.append(test)
#                print("AAA")
                break
            elif i // test < test:
#                print("BBB")
                break
            else:
                div_list.append(test)
                div_list.append(i // test)
        test += 1
    pgi = True
#    print(div_list)
    for div in div_list:
#        print(div + i // div)
        if div + i // div not in prime:
            pgi = False
            break
    if pgi:
        print("ADD : ", i)
        sum += i
print(sum)