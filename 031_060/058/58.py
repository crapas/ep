def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime = 0
non_prime = 1

n = 2
while True:
    new_element = [(2 * n - 1) ** 2, (2 * n - 1) ** 2 - 2 * (n - 1), (2 * n - 1) ** 2 - 4 * (n - 1), (2 * n - 1) ** 2 - 6 * (n - 1)]
    for e in new_element:
        print(e)
        if is_prime(e):
            prime += 1
        else:
            non_prime += 1
    if prime / (prime + non_prime) < 0.1:
        print(2 * n - 1)
        break
    n += 1



