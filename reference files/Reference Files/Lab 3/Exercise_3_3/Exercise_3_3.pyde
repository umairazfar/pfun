#Using loops and conditionals, fill your entire screen first with slant lines, all equally spaced and equally tilted, then fill your entire screen with lines this time oppositely tilted from the previous one. This should create a diamond shaped texture.

def setup(): 
  size(500,500)

def draw(): 
    x = -500
    y = 1000
    background(113, 45, 68)
    for i in range(0, 500):
        stroke(y, x, i)
        line(x , 0, 500, y)
        line(0, y, y, 0)
        x = x + 20
        y = y - 20