def is_inc(n):
    n_str = str(n)
    for i in range(0, len(n_str) - 1):
        if n_str[i] > n_str[i + 1]:
            return False
    return True

def is_dec(n):
    n_str = str(n)
    for i in range(0, len(n_str) - 1):
        if n_str[i] < n_str[i + 1]:
            return False
    return True
b_c = 0
upper = 1000
for i in range(1, upper + 1):
    if not(is_inc(i) or is_dec(i)):
        b_c += 1

i = 0
b_c = 0
while True:
    i += 1
    if not(is_inc(i) or is_dec(i)):
        b_c += 1
    if b_c / i == 0.525:
        print(i)
    if b_c / i == 0.99:
        print(i)
        break


print(b_c / upper)

