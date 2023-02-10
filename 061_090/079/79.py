with open("keylog.txt", "r") as rp:
    lines = rp.readlines()
after = {}
for i in range(0, 10):
    after[i] = set()
for line in lines:
    n1 = int(line[0])
    n2 = int(line[1])
    n3 = int(line[2])
    after[n1].add(n2)
    after[n1].add(n3)
    after[n2].add(n3)

zero_idx = []
for i in range(0, 10):
    if after[i] == 0:
        zero_idx.append(i)

for idx in zero_idx:
    after.pop(idx)    

cur_len = 1
result = ""
while True:
    idx = -1
    pop_idx = -1
    for k, v in after.items():
        if len(v) == cur_len:
            if cur_len == 1:
                result = str(list(v)[0])
            result = str(k) + result
            pop_idx = k
            break
    after.pop(k)
    cur_len += 1
    if len(after) == 0:
        break

print(result)
#73162890