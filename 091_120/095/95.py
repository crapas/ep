def proper_divisor(n):
    sum = 1
    divi = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            sum += n // i
    return sum


max_len = 0
small_member = -1
for i in range(1, 1000001):
#for i in range(1, 1000):
    #print(i)    
    chain = []
    n = i
    while True:
        if n > 1000000:
            break
        chain.append(n)
        n = proper_divisor(n)
        if n in chain:
            if n != chain[0]:
                break
#            if n != chain[0]:
#                break
            chain_len = len(chain)
            if chain_len > max_len:
                max_len = chain_len
                small_member = min(chain)
                print(i, " == >", max_len, small_member)
                print(chain)
            break
print(max_len, small_member)

print(proper_divisor(220))