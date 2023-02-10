with open("triangles.txt", "r") as rp:
    lines = rp.readlines()
def areatest(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0:
        print(x1, y1)
    if x2 == 0 and y2 == 0:
        print(x2, y2)
    if x1 == x2:
        largey = max(y1, y2)
        smally = min(y1, y2)
        if (largey - x1) * (smally - x1) <= 0:
            return 1
        else:
            return 0
    m = (y2 - y1) / (x2 - x1)
    a = y1 - m * x1
    start = max(min(x1, x2), 0)
    end = max(x1, x2)
    if end < 0:
        return 0
    c1 = start * m + a - start
    c2 = end * m + a - end
#    print(x1, y1, x2, y2, start, end, c1, c2)
    if c1 * c2 <= 0:
        return 1
    return 0

def check(x1, y1, x2, y2, x3, y3):
    if x1 == y1 or x2 == y2 or x3 == y3:
        print(x1, y1, x2, y2, x3, y3)
    cnt = 0
    cnt += areatest(x1, y1, x2, y2)
    cnt += areatest(x1, y1, x3, y3)
    cnt += areatest(x2, y2, x3, y3)
    return cnt

sum = 0
for line in lines:
    seg = line.strip().split(",")
    x1 = int(seg[0])
    y1 = int(seg[1])
    x2 = int(seg[2])
    y2 = int(seg[3])
    x3 = int(seg[4])
    y3 = int(seg[5])
    result = check(x1, y1, x2, y2, x3, y3)
    if result == 1:
        sum += 1
print(sum)