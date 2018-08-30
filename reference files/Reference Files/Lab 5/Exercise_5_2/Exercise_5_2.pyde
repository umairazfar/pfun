#Write a function to draw a shape of your choice. Use it to draw the same shape to the screen multiple times, each at a different position using Recursion.

def setup():
    size(500, 500)
    background(78)
    shapes(50,100)
    
def shapes(x,y):
    rect(x, y, 50, 50)
    while x >0 and y <500:
        shapes(x +10  ,y+5)


    