# 1st : 2 + 1 / (1)
# 2s5 : 2 + 1 / (1...

def sumdigit(n):
    str_n = str(n)
    sum = 0
    for c in str_n:
        sum += int(c)
    return sum

def ifv(n):
    if n % 3 == 2:
        return (n // 3 + 1) * 2
    else:
        return 1


def addone(p, u, d):
    # result = p + u/d  = pd/d + u / d = (pd + u)/d
    return p * d + u, d

def cal(n):
    u = 0
    d = 0
    if n == 99:
        return ifv(n), 1
    u, d = cal(n + 1)
    return ifv(n) * u + d, u


u, d = cal(1)
rd = u
ru = 2 * rd + d
print(u, d)
#ru = 2 * d + u
print(ru, rd)
v = sumdigit(ru)
print(v)
print(sumdigit(u), sumdigit(d))
    

#    if n == 10:
#        return p, 1
#    else:
#        d, u = addone(p, u, d)
         


