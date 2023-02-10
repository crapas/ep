min_sq = 1020304050607080900
max_sq = 1929394959697989990

def is_right(n):
    if n % 10 == 0 and n // 100 % 10 == 9 and n // 10000 % 10 == 8 and n // 1000000 % 10 == 7 and n // 100000000 % 10 == 6 and n // 10000000000 % 10 == 5 and n // 1000000000000 % 10 == 4 and n // 100000000000000 % 10 == 3 and n // 10000000000000000 % 10 == 2:
        return True
    else:
        return False
'''
    templete = "1_2_3_4_5_6_7_8_9_0"
    n_str = str(n)
    new_str = ""
    for i in range(0, len(n_str)):
        if i % 2 == 1:
            new_str += "_"
        else:
            new_str += n_str[i]
    if templete == new_str:
        return True
    return False
'''

min_v = int(min_sq ** 0.5)
max_v = int(max_sq ** 0.5) + 1
print(max_v - min_v)
for i in range(min_v, max_v):
    if i % 10 == 0:
        if is_right(i ** 2):
            print(i)
