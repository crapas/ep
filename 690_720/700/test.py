m_key = 4503599627370517
en = 1504170715041707

def prime_factor(n):
    print("prime_factor ", n)
    factor_list = []
    i = 2
    while n != 1:
        if n % i == 0:
            factor_list.append(i)
            n = n // i
            print(i)
        else:
            i += 1
    return factor_list


print(prime_factor(m_key))
print(prime_factor(en))