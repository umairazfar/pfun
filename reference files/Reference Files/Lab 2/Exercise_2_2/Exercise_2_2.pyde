'''Exercise 2.2 Your program automatically saves the width and height of your window. Anywhere
in your program if you call width or height, your program will refer to values of the width
and height that you input in your size() function.
Setup a new window which is 400 pixels wide and 500 pixels high. Initiate a variable and assign
it a value of 1. Call the rect() function with the first two parameters set as the variable name and
set its width and height to half the window size. As your program runs, keep incrementing your
variable by 10.
Your program should construct a series of rectangles drawn diagonally on your drawing window.
'''

def setup():
    size(400, 500)
    
x = 1
def draw():
    global x
    rect(x , x, width/2, height/2)
    x = x + 10 