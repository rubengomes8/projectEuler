class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.selected = False
def create_empty_pyr(height):
    pyr = [[]]*height
    return pyr

def fill_pyr(data, pyr):
    index = 0
    for string in data:
        list = string.split(" ")
        length = len(list[len(list)-1])
        list[len(list) - 1] = list[len(list) - 1][0:length-1]
        print(list)
        pyr[index] = list
        index += 1
    return pyr

def main():
    with open("problem18.txt", "r") as f:
        data = f.readlines()
        print(data)
        print(len(data))
        pyr = create_empty_pyr(15)
        pyr = fill_pyr(data, pyr)
        print(pyr)
        root_bool = True
        for i in range(0, 14):
            col = 0
            for j in range(0, len(pyr[i])):
                if root_bool:
                    root_bool = False
                    left = Node(None, None)
                    right = Node(None, None3)
                    root = Node(pyr[i+1][j], pyr[i+1][j+1])


            #print(str(line_up))
            #print(str(line_down))

        # processar última linha


        f.close()


if __name__ == "__main__":
    main()
