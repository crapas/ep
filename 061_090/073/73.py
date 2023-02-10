upper = 12000
#upper = 8
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

cnt = 0
for i in range(5, upper + 1):
    
    start = i // 3 + 1
    end = i // 2
    if i % 2 == 0:
        end -= 1
    
    for j in range(start, end + 1):
        if gcd(j, i) == 1:
            cnt += 1

print(cnt)
