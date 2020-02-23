import time

start_time = time.time()

def create_empty_pyr(height):
    pyr = [[]] * height
    return pyr


def fill_pyr(data, pyr):
    index = 0
    for string in data:
        list = string.split(" ")
        length = len(list[len(list) - 1])
        list[len(list) - 1] = list[len(list) - 1][0:length - 1]
        print(list)
        pyr[index] = list
        index += 1
    return pyr


def main():
    with open("problem67.txt", "r") as f:
        data = f.readlines()
        print(data)
        print(len(data))
        height = 100
        pyr = create_empty_pyr(height)
        pyr = fill_pyr(data, pyr)
        print(pyr)
        f.close()
        for i in range(height-1, 0, -1):
            for j in range(0, len(pyr[i])-1):
                pyr[i-1][j] = max(int(pyr[i][j]), int(pyr[i][j+1])) + int(pyr[i-1][j])

        print(pyr[0][0])
        print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()