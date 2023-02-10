
import random


prime_list = [2, 3, 5]
not_prime_list = [0, 1, 4]

def is_prime(n, k = 3):    
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        not_prime_list.append(n)
        return False
    else:
        s, d = 0, n - 1
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        # A for loop with a random sample of numbers
        for a in random.sample(range(2, n-2), k):
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        not_prime_list.append(n)
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    not_prime_list.append(n)
                    return False  # composite if we reached end of this loop
        prime_list.append(n)
        return True  # probably prime if reached end of outer loop

def check2(i, j):
    if i == 5 or j == 5:
        return False
    if not is_prime(int(str(i) + str(j))):
        return False
    if not is_prime(int(str(j) + str(i))):
        return False
    return True

def check(n, i):
    if 5 in n:
        return False

    for j in n:
        if not is_prime(int(str(i) + str(j))):
            return False
        if not is_prime(int(str(j) + str(i))):
            return False
    return True

i = 2
p_4s = []
p_3s = []
p_2s = []
goon = True

while goon:
    i += 1
    if i % 100 == 0:
        print(i, len(p_2s), len(p_3s), len(p_4s))
    if is_prime(i):
        for p_4 in p_4s:
            if check(p_4, i):
                print(p_4, i)
                goon = False
#                print(p_4[0] + p_4[])
        for p_3 in p_3s:
            if check(p_3, i):
                p_4s.append((p_3[0], p_3[1], p_3[2], i))
                print("ap - p_4 : ", p_3, i)
        for p_2 in p_2s:
            if check(p_2, i):
                p_3s.append((p_2[0], p_2[1], i))
                print("ap - p_3 : ", p_2, i)
        for p in prime_list:
            if p < i:
                if check2(p, i):
                    p_2s.append((p, i))



# prime이냐?
# p_4와 검사. 통과하면 OK
# p_3와 검사. 통과하면 P_4에 추가
# p_2와 검사. 통과하면 P_3에 추가
# p와 검사. 통과하면 P_2에 추가

# 과거의 prime들과 pair가 되는지 확인. pair가 된다면 p_2에 tuple을 추가
# p_2에 추가를 해 보고... p_3가 되는지를 확인. P


'''
for i in range(1, 100000):
    p = is_prime(i)
    if i % 1000 == 0:
        print(i, p)

l_len = len(prime_list)

p_tuple = []
for i1 in range(1, l_len):
    print(i1, l_len, len(p_tuple))
    for i2 in range(i1 + 1, l_len):
        if check2(i1, i2):
            p_tuple.append((i1, i2))
    
'''

#print(prime_list[0:100])
#print(not_prime_list[0:100])
'''
l_len = len(prime_list)
#print(l_len)
for i1 in range(1, l_len):
    print(l_len, i1)
    for i2 in range(i1 + 1, l_len):
        for i3 in range(i2 + 1, l_len):
            for i4 in range(i3 + 1, l_len):
                for i5 in range(i4 + 1, l_len):
                    check_arr = [prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4], prime_list[i5]]
                    
                    v = check(check_arr)
                    if v:
                        print(check_arr, v)

'''