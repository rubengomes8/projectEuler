'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import numpy as np

def sum_divisors(j):
    soma = 1
    for i in range(2, int(j/2+1)):
        if j % i == 0:
            soma += i

    return soma


sum_array = np.zeros(dtype=int, shape=10000)

for i in range(2, 10000):
    sum_array[i] = sum_divisors(i)

print(sum_array)

sum_amicable = 0

for i in range(2, 10000):
    j = sum_array[i]
    if j <= 9999 and j != i:
        if sum_array[j] == i:
            print(j, i)
            sum_amicable += i

print(sum_amicable)