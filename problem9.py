# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

# sqrt(1000) = 31.6

for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a + b + c == 1000:
                if a*a + b*b == c*c:
                    print(a, b, c, a*b*c)
                    exit(0)



