def isprime(i):
    for j in range(2, i):
        if i % j == 0:
            return False

    return True

result = 1
for i in range(1, 600851475144):
    if  600851475143 % i == 0:
        if isprime(i):
            result = i

print(result)


#