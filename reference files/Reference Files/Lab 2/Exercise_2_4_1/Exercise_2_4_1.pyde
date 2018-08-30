'''Use Multiplication to create a series of lines with increasing space between each line.
You’ll have to use the line() function for this exercise.
'''

def setup():
    size(400, 500)

x = 1
count= 1
def draw():
    frameRate(5)
    global x
    global count
    line(x*count,0,x*count, 500)
    x = x+1
    count = count * 1.1