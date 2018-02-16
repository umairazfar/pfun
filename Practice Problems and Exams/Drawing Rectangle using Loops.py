#Drawing a rectangle of defined length and width
width = int(input("Enter width: "))
height = int(input("Enter height: "))

for y in range(0, height):
    for x in range(0, width):
        print('*', end = '')
    print()