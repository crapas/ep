# M = 1000
# D = 500
# C = 100
# L = 50
# X = 10
# V = 5
# I = 1
# CD = 400 -> CCCC
# CM = 900 -> CCCCCCCCC
# XL = 40 -> XXXX
# XC = 90 -> XXXXXXXXX
# IX = 9 -> IIIIIIII
# IV = 4 -> IIII

def r2d(roman):
    v = 0
    roman = roman.replace('CD', 'CCCC').replace('CM', 'CCCCCCCCC').replace('XL', 'XXXX').replace('XC', 'XXXXXXXXX').replace('IX', 'IIIIIIIII').replace('IV', 'IIII')
    for c in roman:
        if c == 'M':
            v += 1000
        if c == 'D':
            v += 500
        if c == 'C':
            v += 100
        if c == 'L':
            v += 50
        if c == 'X':
            v += 10
        if c == 'V':
            v += 5
        if c == 'I':
            v += 1
    
    return v

with open('p089_roman.txt', 'r') as rp:
    lines = rp.readlines()
cnt = 0
for line in lines:
    v = r2d(line.strip())
    rd = ''
    #print(line.strip(), v)
    d4 = v // 1000
    d3 = (v % 1000) // 100
    d2 = (v % 100) // 10
    d1 = v % 10
    #print(v, d4, d3, d2, d1)
    for i in range(d4):
        rd += 'M'
    if d3 == 9:
        rd += 'MCM'
    elif d3 == 4:
        rd += 'MCD'
    elif d3 == 8:
        rd += 'DCCC'
    elif d3 == 7:
        rd += 'DCC'
    elif d3 == 6:
        rd += 'DC'
    elif d3 == 5:
        rd += 'D'
    elif d3 == 3:
        rd += 'CCC'
    elif d3 == 2:
        rd += 'CC'
    elif d3 == 1:
        rd += 'C'
    if d2 == 9:
        rd += 'XC'
    elif d2 == 8:
        rd += 'LXXX'
    elif d2 == 7:
        rd += 'LXX'
    elif d2 == 6:
        rd += 'LX'
    elif d2 == 5:
        rd += 'L'
    elif d2 == 4:
        rd += 'XL'
    elif d2 == 3:
        rd += 'XXX'
    elif d2 == 2:
        rd += 'XX'
    elif d2 == 1:
        rd += 'X'
    if d1 == 9:
        rd += 'IX'
    elif d1 == 8:
        rd += 'VIII'
    elif d1 == 7:
        rd += 'VII'
    elif d1 == 6:
        rd += 'VI'
    elif d1 == 5:
        rd += 'V'
    elif d1 == 4:
        rd += 'IV'
    elif d1 == 3:
        rd += 'III'
    elif d1 == 2:
        rd += 'II'
    elif d1 == 1:
        rd += 'I'
    oro = line.strip()
    if oro == rd:
        cnt += 1
    print(oro, v, rd, oro == rd)
print(cnt)