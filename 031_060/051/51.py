p_memo = {}

def is_prime(n):
    if n in p_memo:
        return p_memo[n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p_memo[n] = False
            return False
    p_memo[n] = True
    return True

def sharp_cnt(w):
    cnt = 0
    for c in w:
        if c == '#':
            cnt += 1
    return cnt

def make_case(n, rest):
    if n == 0:
        return rest
    result = []
    returned = make_case(n - 1, rest)
    if isinstance(returned, str):
        result.append("d" + returned)
        result.append("#" + returned)
    else:
        for re in returned:
            result.append("d" + re)
            result.append("#" + re)
    return result

def make_template_old(digit_num, sub_num):
    temp = make_case(digit_num - 1, "")
    result = []
    for r in temp:
        if sharp_cnt(r) == sub_num:
            result.append(r + "d")
    return result

memo = {}
def make_template(n, sc):
    if n -1 < sc:
        return []
    if (n, sc) in memo:
        return memo[(n, sc)]
    result = []
    temp = make_case(n - 1, "")
    for r in temp:
        if sharp_cnt(r) == sc:
            result.append(r + "d")
    memo[(n, sc)] = result
    return result

#    for i in range(3, n_len, 3):
#        temp = make_case(n_len - 1, )




i = 1000
stop = False
while not stop:
    i_str = str(i)
    digit_len = len(str(i))
    for j in range(3, digit_len, 3):
        temp = make_template(digit_len, j)

        for t in temp:
            primecnt = 0
            check = ""
            checksum = 0
            for k in range(digit_len):
                if t[k] == 'd':
                    check += i_str[k]
                    checksum += int(i_str[k])
                else:
                    check += '#'
            if checksum % 3 == 0:
                continue
            p_cnt = 0
            for k in range(10):
                if k == 0 and check[0] == '#':
                    continue
                #replaced = check.replace('#', str(k))
                if is_prime(int(check.replace('#', str(k)))):
                    p_cnt += 1
            if p_cnt == 8:
                print(i)
                print(check)
                stop = True
#                print(replaced)
            
            
    i += 1
