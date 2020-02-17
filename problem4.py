i=999
j=999
highest = 0

def isPalindrome(number):
    nb = str(number)
    i = 0
    j = len(nb) - 1
    while i < j:
        if nb[i] == nb[j]:
            pass
        else:
            return False
    return True

while i != 0:
    while j != 0:
        if isPalindrome(j*i):
            if j*i > highest:
                highest = j*i
        j -= 1
    i -= 1

print(highest)

