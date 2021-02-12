import math

def isprime(i):
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            return False

    return True

result = 1

print(int(600851475143/2))
for i in range(int(600851475143/2), 2, -2):
    if 600851475143 % i == 0:
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0and i % 11 != 0 and i % 13 != 0:
            if isprime(i):
                result = i
                print(i)
                exit(0)

print(result)
