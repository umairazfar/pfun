'''Exercise 2.3 Now initiate 2 more variables and assign them a value of 1. Give a color to your
rectangle using fill(). Use your variables as parameters for fill() and keep incrementing your
variables.
Your program should again construct a series of rectangles drawn diagonally on your drawing
window except that every rectangle now has a different color.'''

def setup():
    size(400, 500)
x = 1
y = 1
z = 1
def draw():
    global x
    global y
    global z
    frameRate(5)
    fill(x,y,z)
    stroke( y * 3.3 + 16)
    rect(x , x, width/2, height/2)
    x = x + 10 
    y = y + 1.5 * 2.3
    z = x / y + x