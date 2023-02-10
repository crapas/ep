import math
def test_p_num(n):
    #print(n)
    sol = (1 + math.sqrt(1 + 24 * n)) % 6
    #print(sol)
    if sol == 0:
    #    print("=== >", n)
        return True
    return False

i = 1
stop = False
while not stop:
    #print(i)
    pi = i * (3 * i - 1) // 2
    for j in range(1, i):
        #print(i, j)
    #for j in range(i - 1, 0, -1):
        pj = j * (3 * j - 1) // 2
        sum = pi + pj
        diff = pi - pj
#        print(sum, diff)
        if test_p_num(sum) and test_p_num(diff):
            print(diff)
            stop = True
            break
    i += 1
    #if i == 10: break
