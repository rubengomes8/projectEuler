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
'''

import time
import pandas as pd
import numpy as np
import math


def p10(n):
    numbers = list(range(2, n + 1, 1)) # cria lista de 2 a 2M
    df = pd.DataFrame(np.array(numbers), columns=['n'])
    print(df)
    i = 2
    cnt = 0
    while i < math.sqrt(n):
        idx = list(range(i, n + 1, i)) # cria uma lista com os múltiplos de i
        f_idx = idx[0]
        idx = idx[1:]
        df.n.iloc[np.array(idx) - 2] = np.nan
        aux = df.loc[f_idx - 2 + 1:, 'n']
        i = int(aux[aux.first_valid_index()])
        cnt += 1

    df = df.dropna()
    sum_primes = df.sum()
    return sum_primes


if __name__ == '__main__':
    start_time = time.time()
    result = int(p10(2000000))
    end_time = time.time()
    print(end_time - start_time)
    print(result)






