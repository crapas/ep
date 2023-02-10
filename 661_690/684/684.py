mod_v = 1000000007


def s(n):
    sn = ((n - 1) % 9 + 2) * 10 ** ((n - 1) // 9) - 1
   
    return sn % mod_v

memo = {}
memo[0] = 0
def S(n):
#    print("for ", n)
    last_keys = max(memo.keys())
    last_value = memo[last_keys]
#    print("last : ", last_keys, last_value)
    if n <= last_keys:
        return -1
    sum = last_value
    for i in range(last_keys + 1, n + 1):
#        print("+ ", i, s(i))
        sum += s(i)
        sum = sum % mod_v
    
    memo[n] = sum % mod_v
    return sum % mod_v

#print(S(5))
#print(S(20))
f = [0, 1]
for i in range(100):
    f.append(f[-1] + f[-2])
sum_c = 0
for i in range(2, 91):
    print(i)
#    print("~~~", f[i])
    sum_c += S(f[i])
    sum_c = sum_c % mod_v
#    print(f[i])
print("=====", sum_c)
'''
sum = 0
sum += S(1)
sum += S(2)
sum += S(3)
S(4)
sum += S(5)
S(6)
S(7)
sum += S(8)
print(sum)

for i in range(2, 91):
    print(i, f[i], S(f[i]))
'''