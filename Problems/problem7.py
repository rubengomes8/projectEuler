counter = 1
cur = 3
def isprime(i):
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            return False
    return True
while counter != 10001:
    if isprime(cur):
        counter += 1
        if counter == 10001:
            print(cur)
    cur += 2