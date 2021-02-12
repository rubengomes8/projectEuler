'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time

start_time = time.time()

total = 1
for i in range(1, 101):
    total *= i

str_total = str(total)
print(str_total)
sum = 0
for i in range(0, len(str_total)):
    sum += int(str_total[i])

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))

