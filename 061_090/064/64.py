# r(a) = n + r(a) - n
# = n + 1 / (1 / (r(a) - n))
# = n + 1 / ((r(a) + n)/(a - n ** 2))


import math
upper = 10000
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# (r(x) - y) / z
def next(x, y, z):
    # z / (r(x) - y) = z * (r(x) + y) / (x - y * y)
    di = x - y ** 2
    # = z * (r(x) + y) / di
    di = di // z
    # = (r(x) + y) / di
    t = y
    a = 0 
    while True:
        a += 1
        t -= di
        if x ** 0.5 + t - di <= 0:
            break
    # a + (r(x) + t) / di

    return a, x, -t, di
'''
    # z / (r(x) - y) =  z * (r(x) + y) / (x - y * y)
    a = math.floor((x ** 0.5 - y) / z)
    di = x - y ** 2
    gc = gcd(z, di)
    print(z, di, gc)
    z = z // gc
    di = di // gc
    # (r(x) + y) / di
    # (r(x) + y) / di - a
    # = (r(x) + y - a*di) / di
    print("a : ", a, " di : ", di)

    if z != 1:
        print("Z is not 1!!!!")

    return a, x, y - a * di, di

    print(int_part)
'''
#next(23, 0, 1)
odd_cnt = 0
for i in range(1, upper + 1):
    if i ** 0.5 == int(i ** 0.5):
        continue
    memo = []
    a0 = math.floor(i ** 0.5)
    #print(a0)
    b0_x = i
    b0_y = a0
    b0_z = 1
    a = a0
    x = b0_x
    y = b0_y
    z = b0_z
    findidx = -1
    while True:

        if (x, y, z) in memo:
            for idx, v in enumerate(memo):
                if v == (x, y, z):
                    findidx = idx
            break
        else:
            memo.append((x, y, z))
    #for i in range(10):
        #print(a, x, y, z)
        a, x, y, z = next(x, y, z)

#    print(i, len(memo) - findidx)
    cnt = len(memo) - findidx
    if cnt % 2 == 1:
        odd_cnt += 1

print(odd_cnt)


