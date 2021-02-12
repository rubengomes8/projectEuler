'''
file containing over five-thousand first names, begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.

So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

with open("problem22.txt", "r") as f:
    dict_points = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    data = f.readlines()
    #print(data)
    list_names = data[0].split('","')
    #print(list_names)
    list_names[0] = list_names[0][1:]
    list_names[-1] = list_names[-1][0:-1]
    # print(list_names)
    list_names.sort()
    #print(list_names)

    total = 0
    for i in range(0, len(list_names)):
        sum_in = 0
        for j in range(0, len(list_names[i])):
            sum_in += dict_points[list_names[i][j]]

        total += sum_in * (i+1)

    print(total)


