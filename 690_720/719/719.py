def split_string(w):
    result = [(w,)]
    w_len = len(w)
    if w_len == 1:
        return result
    else:
        for i in range(1, w_len):
            post_segments = split_string(w[i:])
            for seg in post_segments:
                result.append((w[:i],) + seg)
    return result

templete_memo = {}

def split_n(n):
    n_str = str(n)
    n_len = len(n_str)

    if n_len in templete_memo:
        templete = templete_memo[n_len]
    temp_base = ""
    for i in range(n_len):
        temp_base += '#'
    templete = split_string(temp_base)
    templete_memo[n_len] = templete
    result = []
    for tls in templete:
        element = ()
        consume = 0
        for tl in tls:
            tl_len = len(tl)
            seg = n_str[consume:consume + tl_len]
            element = element + (seg,)
            consume += tl_len
        result.append(element)
    #print(templete)
    #print(result)
    return result

#split_n(124355555)

result = 0
N = 10 ** 4
#N = 10 ** 12
i = 1
before = -1
while True:
    sn = i ** 2
    sn_len = len(str(sn))
    if sn_len != before:
        print(sn_len)
        before = sn_len
    if sn > N:
        break
    substrings = split_n(sn)
#    substrings = split_string(str(sn))
    for substring in substrings:
        if len(substring) == 1:
            continue
        sum_v = 0
        for n_w in substring:
            sum_v += int(n_w)
        if sum_v ** 2 == sn:
            result += sn
            break
    i += 1
print(result)
