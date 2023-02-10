frac = []

for i in range(1, 188519):
    i_str = str(i)
    for c in i_str:
        frac.append(int(c))

print(len(frac))
sol = 1
for i in range(7):
    result = frac[10 ** i - 1]
    print(result)
    sol *= result

print(sol)