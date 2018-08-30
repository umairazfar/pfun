#Modify the previous code such that when your line reaches one edge of your screen, it starts move in the opposite direction.

def setup():
    size(400, 500)

x  = 0
y = 400
def draw():
    global x
    global y
    frameRate(30)
    background((y - x) / 4)
    if x <400:
        line(x, 0, x, 500)
        x = x + 2
    elif x >= 400:
            line(y , 0 , y, 500)
            y = y -2
            if y <=0:
                x = 0
                y = 400