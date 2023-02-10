def is_right(n_str):
    if '3' in n_str and '4' in n_str and '5' in n_str and '6' in n_str and '7' in n_str:
        return True
    else:
        return False
    
def p3(n):
    return n * (n + 1) // 2

def p4(n):
    return n * n

def p5(n):
    return n * (3 * n - 1) // 2

def p6(n):
    return n * (2 * n - 1)

def p7(n):
    return n * (5 * n - 3) // 2

def p8(n):
    return n * (3 * n - 2)

    
i = 1
p3l = []
p4l = []
p5l = []
p6l = []
p7l = []
p8l = []

while True:
    p = p4(i)
    if p >= 1000 and p < 10000:
        p4l.append(p)
    p = p5(i)
    if p >= 1000 and p < 10000:
        p5l.append(p)
    p = p6(i)
    if p >= 1000 and p < 10000:
        p6l.append(p)
    p = p7(i)
    if p >= 1000 and p < 10000:
        p7l.append(p)
    p = p8(i)
    if p >= 1000 and p < 10000:
        p8l.append(p)
    p = p3(i)
    if p >= 1000 and p < 10000:
        p3l.append(p)
    
    if p >= 10000:
        break
    i += 1

pl = p3l + p4l + p5l + p6l + p7l
print(len(pl))
pl = list(set(pl))
print(len(pl))

x = 0
for e1 in p8l:
#    print("1st loop : " , x)
    x += 1
    y = 0
    h1 = e1 // 100
    t1 = e1 % 100
    for e2 in pl:
#        print("2nd loop : " , y)
        y += 1
        h2 = e2 // 100
        t2 = e2 % 100
        if t1 == h2:
            for e3 in pl:
                h3 = e3 // 100
                t3 = e3 % 100
                if t2 == h3:
                    for e4 in pl:
                        h4 = e4 // 100
                        t4 = e4 % 100
                        if t3 == h4:
                            for e5 in pl:
                                h5 = e5 // 100
                                t5 = e5 % 100
                                if t4 == h5:
                                    for e6 in pl:
                                        h6 = e6 // 100
                                        t6 = e6 % 100
                                        if t5 == h6 and t6 == h1:
                                            check = [False, False, False, False, False]
                                            test = [e2, e3, e4, e5, e6]
                                            note = ""
                                            for t in test:
                                                if t in p3l:
                                                    check[3 - 3] = True
                                                    note += "3"
                                                if t in p4l:
                                                    check[4 - 3] = True
                                                    note += "4"
                                                if t in p5l:
                                                    check[5 - 3] = True
                                                    note += "5"
                                                if t in p6l:
                                                    check[6 - 3] = True
                                                    note += "6"
                                                if t in p7l:
                                                    check[7 - 3] = True
                                                    note += "7"
                                            if False not in check and is_right(note):
                                                res_arr = sorted([e1, e2, e3, e4, e5,e6])
                                                print(res_arr)
                                                print(sum(res_arr))
                                                print(note)





for e8 in p8l:
    tail8 = e8 % 100
    head8 = e8 // 100
