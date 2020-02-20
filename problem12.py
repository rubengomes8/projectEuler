def number_divisors(nb):
    counter = 0
    for i in range(1, int(nb/2) + 1):
        if nb % i == 0:
            counter += 1
    return counter




increment = 1
current = 0
while True:
    current += increment
    increment += 1
    print(current)
    if number_divisors(current) > 499:
        print(current)
        exit(0)
