from math import sqrt
j, cont = 1, 1
while cont == 1:
    for l in range(1,j):
        c = 3 * (l ** 2 + j ** 2) - l - j       # k = i + j
        k = (1 + sqrt(1 + 12*c))/6
        if k == int(k):
            c2 = 3*(k*k + j*j) - k - j          # m = k + j
            m = (1 + sqrt(1 + 12*c2))/6
            if m == int(m):
                print (l*(3*l-1)/2)
                cont = 0
            c2 = 3*(k*k + l*l) - k - l
            m = (1 + sqrt(1 + 12*c2))/6
            if m == int(m):
                print (j*(3*j-1)/2)
                cont = 0
    j += 1