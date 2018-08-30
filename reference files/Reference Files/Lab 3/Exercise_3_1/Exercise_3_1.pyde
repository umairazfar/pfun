'''Exercise 3.1 Use the code in example 3.3 and conditionals to create an animated hypnotizing
pattern.
You will have to use the conditionals to alternately fill your ellipses black and white, and shorten
the distance between every ellipse. Your draw function will give it the hypnotizing effect.
'''
def setup():
    size(500, 500)
count = 0
def  draw():
    global count
    frameRate(15)
    if count % 2 ==0:
        for i in range(800, 0, -10):
            fill(255)
            ellipse(250, 250, count, count)

    else:
        for i in range(800, 0, -10):
            fill(0)
            ellipse(250, 250, count, count)
    count = count +1 