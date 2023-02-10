n = 1070379110490
#n = 10 ** 12 + 7 

i = 0
while True:
    N = n * 2 - 1
    # N always odd 
    B = ((N ** 2 + 1) / 2) ** 0.5
    print(n, B, B % 2)
    if B % 2 == 1:
        print((B + 1) / 2)
        break
    n += 1
    i += 1
    if i == 10:
        break