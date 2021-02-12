'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.

However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import pandas as pd
import numpy as np
import time

start_time = time.time()
'''

def is_abundant(x):
    arr = np.arange(1, int(x/2)+1)
    divisors = np.zeros(len(arr))
    for i in range(1, len(arr)):
        if x % arr[i] == 0:
            divisors[i] = arr[i]

    if sum(divisors) > x:
        return True
    else:
        return False

df_abundant = np.arange(1, int(28124/2+1))
print(df_abundant)

for i in range(1, int(28124/2+1)):
    if not is_abundant(i):
        df_abundant[i-1] = -1

total = 0
df_final = np.arange(1, 28124)
for i in range(1, int(28124/2+1)):
    for j in range(i, int(28124/2+1)):
        if not df_abundant[i-1] == -1 and not df_abundant[j-1] == -1:
            a = i + j
            df_final[a-1] = 0

print(sum(df_final))
'''
def abundant(x):
    arr = np.arange(1, int(x/2)+1)
    divisors = np.zeros(len(arr))
    for i in range(1, len(arr)):
        if x % arr[i] == 0:
            divisors[i] = arr[i]

    if sum(divisors) > x:
        return True
    else:
        return False

# 28124 / 2 = 14062
df_abundants = pd.DataFrame(np.arange(1, 14063), columns=['nb'])
print(df_abundants)

for i in range(1, 14063):
    if abundant(i):
        pass
    else:
        df_abundants['nb'][i-1] = np.nan

df_abundants = df_abundants.dropna()
print(df_abundants)
abundants_ls = df_abundants['nb'].tolist()
print(abundants_ls)

'''
df_final = pd.DataFrame(np.arange(1, 28124), columns=['n'])
for i in range(0, len(abundants_ls)):
    for j in range(i, len(abundants_ls)):
        a = int(abundants_ls[i] + abundants_ls[j])
        df_final['n'][a-1] = np.nan

df_final = df_final.dropna()
final_ls = df_final['n'].tolist()
print(sum(final_ls))
'''
df_final = np.arange(1, 28124)
for i in range(0, len(abundants_ls)):
    for j in range(i, len(abundants_ls)):
        a = int(abundants_ls[i] + abundants_ls[j])
        df_final[a-1] = 0


print(df_final.sum())

print("--- %s seconds ---" % (time.time() - start_time))






