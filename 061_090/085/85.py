def find_rec(n, m):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += (n - i) * (m - j)
    return sum


min = 10000000
standard = 2000000
size = 0

for i in range(2001):
    print(i)
    for j in range(2001):
        v = find_rec(i, j)
        if v > standard:
            diff = v - standard
        else:
            diff = standard - v
        if diff < min:
            min = diff
            size = i * j
        if v > standard:
            break

print(i, j, size, min)