
mindiff = 1
checkmax = 1000000

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_rp(a, b):
    return gcd(a, b) == 1

def nsmall37(n):
    nu = n * 3 // 7
    if not is_rp(n, nu):
        diff = 1
    else:
        diff = 3 / 7 - nu / n
    return nu, diff

min_d = 0
min_n = 0
for i in range(8, checkmax + 1):
    nu, diff = nsmall37(i)
    #print(nu, i, diff)
    if mindiff > diff:
        mindiff = diff
        min_d = i
        min_n = nu
    if i % 10000 == 0:
        print(i, min_n, min_d, mindiff)
    

print("====", min_n, min_d, mindiff)
#print(is_rp(252, 27))
