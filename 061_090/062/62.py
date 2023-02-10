# find smallest cube which exactly five permutations of its digits are cube

def reorder(number):
    number_str_sorted = sorted(str(number))
    ordered_str = ""
    for c in number_str_sorted:
        ordered_str += c
    if ordered_str == "012334556789":
        print(":::", number)
    return ordered_str

permulist = []
permusort_list = []
for i in range(10000):
    permulist.append(i ** 3)

for i in range(10000):
    permusort_list.append(reorder(permulist[i]))

#for i in range(10000):
#    print(permulist[i], permusort_list[i])

permusort_list = sorted(permusort_list)

#print(permusort_list)

last = ""
cnt = 0
for ps in permusort_list:
    if ps == last:
        cnt += 1
    else:
        last = ps
        cnt = 0
    if cnt >= 4:
        print(cnt, ps)