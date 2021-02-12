total = 1
for i in range(0, 1000):
    total *= 2

str_total = str(total)
sum = 0
for i in range(0, len(str_total)):
    sum += int(str_total[i])
print(sum)