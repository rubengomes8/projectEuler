import time

start_time = time.time()


i=999
j=999
highest = 0

def isPalindrome(number):
    nb = str(number)
    i = 0
    j = len(nb) - 1
    while i <= j:
        if nb[i] == nb[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

a = 0
b = 0
while i != 99:
    j=999
    while j != 99:
        if isPalindrome(j*i):
            if j*i > highest:
                highest = j*i
                a=j
                b=i
        j -= 1
    i -= 1

print(highest)
print(a, b)


print("--- %s seconds ---" % (time.time() - start_time))