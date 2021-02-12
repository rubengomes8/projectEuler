# falta terminar a função find_cycle

# irei ignorar o máximo e começar a encontrar o ciclo maior de frente para trás
def find_cycle(nb, size):
    quocient = str(1/nb)
    pat1 = 'a'
    pat2 = 'z'
    print("###########")
    print(quocient)
    for i in range(len(quocient) - 1, -1, -1):
        print(quocient[i])
        
    
    return 20

def largest_cycle(size_max):
    largest = 0
    for i in range(2, 20): # change 20 to 1000
        size = find_cycle(i, size_max)
        if size > largest:
            largest = size
    return largest
    
    
    
def main():
    size_max = 20
    l = largest_cycle(size_max)
    print("Hello World!" + l)

if __name__ == "__main__":
    main()
