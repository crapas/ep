def shcnt(n, view):
    card = []
    nextcard = []
    check = []
    for i in range(n):
        check.append(i)
        card.append(i)
        nextcard.append(i)

    #first shuple
    cnt = 0
    while True:
        cnt += 1
        for i in range(n // 2):
            nextcard[2 * i] = card[i]
            nextcard[2 * i + 1] = card[i + n // 2]
        for i in range(n):
            card[i] = nextcard[i]
        if view: print(card)
        if card == check:
            break
    return cnt

i = 2
sum = 0
while True:
    cnt = shcnt(i, False)
    if cnt == 60 :
        sum += i
        print(i, sum)
    i += 2
#    print(i, shcnt(i, False))