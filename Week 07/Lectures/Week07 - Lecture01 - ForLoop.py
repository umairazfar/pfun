# Prints out the numbers 0,1,2,3,4
##for x in range(5):
##    print(x)
##
### Prints out 3,4,5
##for x in range(3, 6):
##    print(x)

### Prints out 3,5,7
##for x in range(3, 8, 3):
##    print(x)
##
##name = 'Umair'
##
##for alphabet in name:
##    print(alphabet)
##
##for alphabet in name:
##    print(alphabet, end="")

#Exercise01
#how can you print a line of '*' with a different length each time?
#num = int(input("Enter the length = "))

import random


def Rect(width, height):
    for i in range(height):    
        for j in range(width):
            print('*', end='')
        print()

#width = int(input('Enter width= '))
#height = int(input('Enter height= '))
for i in range(random.randint(1,5)):
    Rect(random.randint(1,5),random.randint(1,5))

#Exercise02
#Can you make a rectangle like this?

#******
#*    *
#*    *
#******



    
