mov =    500500507
mov_2 = 1000000000
loop = 500499

i = 1

for j in range(loop):
    print(j)
    i *= 2
    i = i % mov_2



print(i % mov)