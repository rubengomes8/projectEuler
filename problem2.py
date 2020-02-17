import numpy as np

l = np.zeros((10000,), dtype=int)
l[0] = 1
l[1] = 2
total = 2
last = 2
last_index = 1
while last <= 4000000:
    l[last_index + 1] = l[last_index] + l[last_index - 1]
    last = l[last_index + 1]
    last_index += 1
    if last % 2 == 0:
        total += last

print(total)

