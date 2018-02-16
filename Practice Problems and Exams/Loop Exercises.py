#Loop exercises

#copy paste every exercise in your own file and run them to see what happens
#You must understand this code perfectly

#Exercise 1

for x in range(0, 10):
    print(x)

#Exercise 2

for x in range(0, 10):
    print(x, end = '')
	
#Exercise 3

for x in range(0, 10):
    print(x, end = ',')
	
#Exercise 4

for x in range(0, 10):
    if x == 9:
        print(x)
    else:
        print(x, end = ',')

#Exercise 5

for x in range(0, 10):
    print(x * -1, end = ' ')

#Exercise 6

for y in range(0, 10):
    print('y: ', y)
    for x in range(0, 10):
        print(' x:', x, end = '')
    print()

#Exercise 7

for y in range(0, 10):
    for x in range(0, 10):
        print('*', end = '')
    print()
