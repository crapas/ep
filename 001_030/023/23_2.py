
def is_abundant(n):
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    if sum > n:
        return True
    return False

ab_list = []
for i in range(1, 28124):
    if is_abundant(i):
        ab_list.append(i)
sumv = 0
for i in range(1, 28124):
    print(i)
    cansum = False
    for j in ab_list:
        if j >= i:
            break
        if i - j in ab_list:
            cansum = True
            break
    if not cansum:
        sumv += i

print(sumv)

        



