# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# A - B
A = 0
for i in range (1, 101):
    A += i

A = A*A

B = 0
for i in range(1, 101):
    B += i*i

print(A-B)