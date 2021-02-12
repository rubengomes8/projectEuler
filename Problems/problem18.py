class Node:
    def __init__(self, left, right, row, col):
        self.left = left
        self.right = right
        self.row = row
        self.col = col
        self.selected = False

def create_empty_pyr(height):
    pyr = [[]]*height
    selected = [[]]*height
    return pyr, selected

def fill_pyr(data, pyr, selected):
    index = 0
    for string in data:
        list = string.split(" ")
        length = len(list[len(list)-1])
        list[len(list) - 1] = list[len(list) - 1][0:length-1]
        print(list)
        pyr[index] = list
        selected[index] = [False]*(index+1)
        index += 1
    return pyr, selected

def find_highest_path(pyr, selected, height, row, col, path):

    if row == height-1:
        return int(pyr[row][col]), path+pyr[row][col]+ " "

    cost_left = -1
    cost_right = -1

    # go left if selected
    if selected[row+1][col]:
        cost_left, path_left = find_highest_path(pyr, selected, height, row+1, col, " ")

    if selected[row+1][col+1]:
        cost_right, path_right = find_highest_path(pyr, selected, height, row+1, col+1, " ")

    if cost_right == -1 and cost_left == -1:
        return -1, ""

    if cost_left > cost_right:
        return cost_left + int(pyr[row][col]), path_left+pyr[row][col]+ " "
    elif cost_right > cost_left:
        return cost_right + int(pyr[row][col]), path_right+pyr[row][col]+ " "






def main():
    with open("problem18.txt", "r") as f:
        data = f.readlines()
        print(data)
        print(len(data))
        height = 3
        pyr, selected = create_empty_pyr(height)
        pyr, selected = fill_pyr(data, pyr, selected)
        print(pyr)
        print(selected)

        counter = 0

        while counter < height:
            for row in range(counter, height):
                max = 0
                col_max = 0
                entrou = False
                for col in range(0, len(pyr[row])):
                    if not selected[row][col]:
                        if int(pyr[row][col]) > max:
                            entrou = True
                            max = int(pyr[row][col])
                            col_max = col
                if entrou == True:
                    selected[row][col_max] = True
            # Determinar caminho com maior saldo se existir
            found_cost, path = find_highest_path(pyr, selected, height, 0, 0, " ")
            if found_cost == -1:
                pass
            else:
                print(found_cost)
                print(selected)
                print(path)
                exit(0)
            print(selected)
            counter += 1

        f.close()


if __name__ == "__main__":
    main()
