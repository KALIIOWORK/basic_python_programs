# triangle function to print triangle pattern
def triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i, 0, -1):
            print("*", end=' ')
        print("")


# square function
def square(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            if j <= i:
                print("*", end=' ')
            else:
                print("*", end=' ')
        print()


# sand glass function
def sandGlass(rows):
    i = 0
    while i <= rows - 1:
        j = 0
        while j < i:
            # display space
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1:
            print('*', end=' ')
            k += 1
        print()
        i += 1

    i = rows - 1
    while i >= 0:
        j = 0
        while j < i:
            print('', end=' ')
            j += 1
        k = i
        while k <= rows - 1:
            print('*', end=' ')
            k += 1
        print('')
        i -= 1


# pant style function
def pantStyle(rows):
    print("*" * rows, end="\n")
    i = (rows // 2) - 1
    j = 2
    while i != 0:
        while j <= (rows - 2):
            print("*" * i, end="")
            print("_" * j, end="")
            print("*" * i, end="\n")
            i = i - 1
            j = j + 2


def diamond(rows):
    k = 2 * rows - 2
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")

    k = rows - 2

    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("")


print("Welcome to the pattern printer!\n")


print("1. Triangle\n2. Square\n3. Sandglass\n4. Pant Style\n5. Diamond\n")

shape = int(input("Select the shape you would like to print: "))

rows = int(input("Enter number of rows: "))

if shape == 1:
    triangle(rows)
if shape == 2:
    square(rows)
if shape == 3:
    sandGlass(rows)
if shape == 4:
    pantStyle(rows)
if shape == 5:
    diamond(rows)