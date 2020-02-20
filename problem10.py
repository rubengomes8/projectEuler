def isprime(i):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            return False
    return True


sum = 2
for i in range(3, 2000000, 2):
    if isprime(i):
        sum += i

print(sum)