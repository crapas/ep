p_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
import math


def M(p, q, M):
    if p * q > M:
        return 0
#        print("merong")
    # p^n * q^m
    n = 0
    m = 1
    stop = False
    while not stop:
        if p ** (n + 1) * q ** m > M:
            stop = True
        else:
            n += 1
    
    stop = False
    max = p ** n * q ** m
    while not stop:
        if n == 1:
            break
        n = n - 1
        stop = False
        while not stop:
            m += 1
            if p ** n * q ** m > M:
                stop = True
            else:
                new = p ** n * q ** m
                if new > max:
                    max = new
            #if p ** n * q ** (m + 1) > M:
            #    stop = True
    return max
#    print(n, m, max)

sum = 0
p_len = len(p_list)
for i in range(p_len):
    if p_list[i] > 50:
        continue
    for j in range(i + 1, p_len):
        if p_list[j] > 50:
            continue
        
        v = M(p_list[i], p_list[j], 100)
        if v != 0:
            print(p_list[i], p_list[j], v)
            sum += v
print(sum)

#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
