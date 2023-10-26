#✅ Right Triangle Star Pattern

#Number = int(input("Please enter number \n"))



def print_triangle(a):
    for i in range(a + 1):
        for j in range(i):
            print("*", end="")
        print(end="\n")


x = int(input('Enter number of levels: '))
print_triangle(x)