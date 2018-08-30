'''Exercise 7.1 Write a program that takes the area of a square as input, calculates 
the length of each side and writes the length along with the area on a separate file. 
Your setup window should take the length as input for the fill() function to 
fill your respective square and draw a series of squares(diagonally) starting at the top left 
corner of your window with it's dimensions reducing to zero decrementing by 3 at each 
iteration. Your program will stop writing to the file when it's sides becomes zero and 
will completely stop running when the series of square reaches the bottom right of your
 drawing window.
'''
def setup():
    size(500, 500)
    square_area(500)
    
def square_area(area):
    a = 0
    b = 0
    side = sqrt(area)
    background(145, 23, 78)
    while a<height and b<width:
        fill(side)
        rect(a, b, side, side)
        a = a + 20
        b = b + 20
        side = side - 3
    
         
         
         
    