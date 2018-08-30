#Draw a line on your processing window and using conditionals and variables, make it move across the screen.

def setup():
    size(400, 500)

x  = 0
def draw():
    frameRate(30)
    background(255)
    global x
    line(x,0,x,500)
    x = x+2
    