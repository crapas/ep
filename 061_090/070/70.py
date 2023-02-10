prime = []
#upper = 1000000
upper = 10000000
#upper = 8
import random

def is_permuted(i, j):
    if i == 87109:
        print(i, j)
    i_str_sorted = sorted(str(i))
    j_str_sorted = sorted(str(j))
    return i_str_sorted == j_str_sorted

def is_prime(n, k = 3):    
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n % 2 == 0:  # should be faster than n % 2
        #not_prime_list.append(n)
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
                        #not_prime_list.append(n)
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    #not_prime_list.append(n)
                    return False  # composite if we reached end of this loop
        #prime_list.append(n)
        return True  # probably prime if reached end of outer loop


for i in range(upper + 1):
    if i % (upper // 100) == 0:
        print(i // (upper // 100))
    if is_prime(i):
        prime.append(True)
    else:
        prime.append(False)

#for i in range(100):
#    print(i, prime[i])

min = 1000000
n = -1
for i in range(2, upper + 1):
    if i % (upper // 100) == 0:
        print(i // (upper // 100), n, min)
    tuples = []
    if prime[i]:
        tuples.append((i, 1))
    else:
        #print("for ", i)    
        test = i
        j = 1
        last = 0
        cnt = 0
        while test != 1:
            if prime[test] == True:
                j = test            
            while not prime[j]:
                j += 1
            if test % j == 0:
                test = test // j
                if last == j:
                    cnt += 1
                else:
                    if last != 0:
                        tuples.append((last, cnt))
                    last = j
                    cnt = 1
            else:
                j += 1
        tuples.append((last, cnt))
    v = 1
    for tup in tuples:
        v = v * (tup[0] ** tup[1] - tup[0] ** tup[1] // tup[0])
    if is_permuted(i, v):
        ratio = i / v
#        print(i, v, ratio)
        if min > ratio:
            min = ratio
            n = i
#    print(i, v)

print(n, min)


