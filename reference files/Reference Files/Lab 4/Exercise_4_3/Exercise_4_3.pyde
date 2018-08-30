'''Exercise 4.3 You can use the additive property of rotations and translations to continuously
rotate a line and create a circle. The example code in 4.7 is one way of using the rect() function
to create a circle.
Your task is to use the line() function to create a color wheel such that the colors merge into
each other. Your wheel may not include all the colors.
'''
def setup():
    size(200, 200)
def draw():
    x = 67
    y = 0
    z = 34

    translate(100,100)
    for i in range(0, 450):

        stroke(i*0.9,y/2,z*1.8)
        line(-91, -9, 90,11)
        rotate(-PI/440)
        x = x + 20 
        y = y + 0.8
        z = z - 7.0