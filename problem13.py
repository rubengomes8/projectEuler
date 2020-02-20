with open("problem13.txt", "r") as f:
    data = f.readlines()
    print(data)

# Calcule os dez primeiros dígitos da soma dos seguintes cem números de 50 dígitos.
sum = 0

for string in data:
    _str = string[0:50]
    sum += int(_str)

sum_string = str(sum)
print(sum_string[0:10])
