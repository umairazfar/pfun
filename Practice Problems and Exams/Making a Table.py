temp = input("Add number of rows:")
if (temp == ""):
    rows = 4
else:
    rows = int(temp)

columns = int(input("Add number of columns:"))
width = int(input("Add width:"))
height = int(input("Add height:"))

for j in range(rows * height):
    if j%height == 0:
        for i in range(columns * width):
            if i%width == 0 :
                print("+", end = "")
            else:
                print("-", end = "")
        print("+")
    else:
        for i in range(columns * width):
            if i%width == 0 :
                print("|", end = "")
            else:
                print(" ", end = "")
        print("|")


for i in range(columns * width):
    if i%width == 0 :
        print("+", end = "")
    else:
        print("-", end = "")
print("+")

#This code can further be improved and made smaller. Can you figure out how?

#The width and height values are always 1 less than the asked values, change the code appropriately