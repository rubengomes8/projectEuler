def count(string):
    return len(string)

# Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
dict_units = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
dict_tens = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
dict_more = {"0": "", "2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

total = 0

for i in range(1, 1001):
    string_i = str(i)
    if len(string_i) == 4: # one thousand
        total += 11
        print(total)
        exit(0)
    if len(string_i) == 1:
        total += count(dict_units[string_i])
        print(dict_units[string_i])
    if len(string_i) == 2:
        if string_i[0] == '1':
            total += count(dict_tens[string_i])
            print(dict_tens[string_i])
        else:
            string = dict_more[string_i[0]]+dict_units[string_i[1]]
            total += count(string)
            print(string)
    if len(string_i) == 3:
        if string_i[1] == '0':
            if string_i[1:3] == '00':
                string = dict_units[string_i[0]]+"hundred"
                total += count(string)
                print(string)
            else:
                string = dict_units[string_i[0]]+"hundredand"+dict_units[string_i[2]]
                total += count(string)
                print(string)
        elif string_i[1] == '1':
            string = dict_units[string_i[0]]+"hundredand"+dict_tens[string_i[1:3]]
            total += count(string)
            print(string)
        else:
            string = dict_units[string_i[0]]+"hundredand"+dict_more[string_i[1]]+dict_units[string_i[2]]
            total += count(string)
            print(string)

print(total)

