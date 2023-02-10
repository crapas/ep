limit = 1000000000
# 333333333, 333333333, 333333332 is max
# 333,333,333

sum = 0
i = 1
while True:
    if i % 10000000 == 0:
        print(limit / i)
    a = i
    b = i - 1
    if a + a + b > limit:
        break
    area = b / 2 * (a ** 2 - b ** 2 / 4) ** 0.5
    if area > 0 and area == int(area):
        sum += a + a + b
#        print(i, sum)
    b = i + 1
    if a + a + b > limit:
        break
    area = b / 2 * (a ** 2 - b ** 2 / 4) ** 0.5
    if area > 0 and area == int(area):
        sum += a + a + b
#        print(i, sum)
    i += 1

print(sum)