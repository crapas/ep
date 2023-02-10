
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 720 * 7
    elif n == 8:
        return 720 * 7 * 8
    elif n == 9:
        return 720 * 7 * 8 * 9

def fact_sum(n):
    sum = 0
    while n != 0:
        sum += factorial(n % 10)
        n = n // 10
    return sum

cnt = 0
for i in range(1, 1000000):
    chain = []
    n = i
    chain_cnt = 0
    while True:
        if n not in chain:
            chain_cnt += 1
            chain.append(n)
            n = fact_sum(n)
        else:
            break
    if chain_cnt == 60:
        print(i, chain)
        cnt += 1

print(cnt)