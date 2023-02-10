import math

max = 0
i = 1
line_idx = -1
with open("base_exp.txt", "r") as rp:
    while True:
        line = rp.readline()
        if not line: break
        line_seg = line.strip().split(",")
        base = int(line_seg[0])
        exp = int(line_seg[1])

        v = exp * math.log10(base)
        if v > max:
            max = v 
            line_idx = i
        i += 1
print(line_idx)
