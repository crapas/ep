
cnt = 0
total = 0
p_case = []
c_case = []
for i1 in range(1, 7):
    for i2 in range(1, 7):
        for i3 in range(1, 7):
            for i4 in range(1, 7):
                for i5 in range(1, 7):
                    for i6 in range(1, 7):
                        c_case.append(i1 + i2 + i3 + i4 + i5 + i6)

for i1 in range(1, 5):
    for i2 in range(1, 5):
        for i3 in range(1, 5):
            for i4 in range(1, 5):
                for i5 in range(1, 5):
                    for i6 in range(1, 5):
                        for i7 in range(1, 5):
                            for i8 in range(1, 5):
                                for i9 in range(1, 5):
                                    p_case.append(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9)

print(len(c_case))
print(len(p_case))

p_c = 0
for p in p_case:
    p_c += 1
    print(p_c)
    for c in c_case:%
        total += 1
        if p > c:
            cnt += 1

print(total, cnt)
