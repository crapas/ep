def is_prime(n):
    o = n
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
#            if o == 301:
#                print(n, " %", i)
            return False
    return True


def is_palindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

pairs = []
#print(is_prime(301))

i = 1
while True:
    i += 2
    if not is_prime(i):
        continue
    test = i ** 2
#    if test == 10609:
#        print("Find it")
    if is_palindromic(test):
#        if test == 10609: print("Out1")
        continue
    r_test = int(str(test)[::-1])
    root_r_test = int(r_test ** 0.5)

#    if test == 10609:
#        print("###", r_test ** 0.5, root_r_test)
#        print(root_r_test == r_test ** 0.5)
#        print(is_prime(root_r_test))
    if root_r_test == r_test ** 0.5 and is_prime(root_r_test):
 #       if test == 10609:
 #           print("Find it 2")
        pairs.append(test)
        print(test, len(pairs), int(test ** 0.5), r_test, root_r_test)
#        if test < root_r_test:
#            pair = (test, root_r_test)
#        else:
#            pair = (root_r_test, test)

    if len(pairs) == 50:
        break
print(sum(pairs))            



