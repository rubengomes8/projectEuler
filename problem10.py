'''
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
'''
'''
import pandas as pd

def isprime(i):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            return False
    return True

df = pd.DataFrame(index=list(range(1, 2000000)))
sum = 2

for i in range(2, 2000000):
    if isprime(i):
        for j in range(i, 2000000):
            df.
'''

import numpy as np

array = np.arange(0, 2000000)
print(array)

def isprime(i):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            return False
    return True
sum = 1

for i in range(2, 2000000):
    if array[i] != -1:
        if isprime(i):
            print(i)
            sum += 1
            for j in range(i, 2000000, i):
                array[j] = -1

print(sum)




