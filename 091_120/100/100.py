import sys
c = 10 ** 12

i = 7 *  10 ** 11 + 7 * 10 ** 9 + 1 * 10 ** 8 + 6 * 10 ** 6 + 7 * 10 ** 5 + 81187
min = sys.maxsize
while True:
    root = 8 * i ** 2 - 8 * i + 1
    sol = (1 + root ** 0.5) / 2
#    sol = root - (2 * c - 1) ** 2
    diff = root ** 0.5 - int(root ** 0.5)
    if sol == int(sol):
        if diff < min:
            min = diff
            print(sol, i, min)
    
    if min == 0:
        print(i)
        break
    i += 1
print(i, sol, i / int(sol) * (i - 1) / (int(sol) - 1))
#    if root ** 0.5 == int(root ** 0.5):
#        print(i)
#        break
