# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

def count(i):
    counter = 0
    cur = i
    while cur != 1:
        if cur % 2 == 0:
            cur = cur/2
        else:
            cur = 3*cur + 1
        counter += 1
    return counter


longest = (1, 0) # (starting_nb, counter)

total = 0
for i in range(1, 1000000):
    total = count(i)
    if total > longest[1]:
        longest = (i, total)

print(longest)