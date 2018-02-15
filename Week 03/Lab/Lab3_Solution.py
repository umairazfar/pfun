
import turtle
import math
import random
canvas=turtle.Canvas()
tobi=turtle.Turtle()
tobi.shape('turtle')
tobi.color('red','blue')
tobi.pensize(2)

tobi.hideturtle()
tobi.penup()
tobi.goto(-100,0)
tobi.rt(270)
tobi.showturtle()
tobi.pendown()
degrees = 0
while(degrees <= 20):
    angle = math.cos(degrees*3.1415/180)
    tobi.lt(degrees)
    tobi.penup()
    tobi.fd(9)
    tobi.pendown()
    tobi.fd(1)
    degrees = degrees + 0.1

turtle.reset()

tobi.hideturtle()
tobi.penup()
tobi.goto(-100,0)
tobi.rt(360)
tobi.showturtle()
tobi.pendown()
degrees = 0
while(degrees <= 20):
    angle = math.cos(degrees*3.1415/180)
    tobi.lt(degrees)
    tobi.penup()
    tobi.fd(9)
    tobi.pendown()
    tobi.fd(1)
    degrees = degrees + 0.1

turtle.reset()

tobi.hideturtle()
tobi.penup()
tobi.goto(-100,0)
#tobi.rt(0)
tobi.showturtle()
tobi.pendown()
degrees = 0
while(degrees <= 360):
    color = str(random.randint(1, 4))
    if color == '1' or color == 'red':
        color = 'red'
    elif color == '2' or color == 'green':
        color = 'green'
    elif color == '3' or color == 'blue':
        color = 'blue'
    elif color == '4' or color == 'orange':
        color = 'orange'
    else:
        color = 'gray'

    linecolor = str(random.randint(1, 5))

    if linecolor == '1' or linecolor == 'red':
        linecolor = 'red'
    elif linecolor == '2' or linecolor == 'green':
        linecolor = 'green'
    elif linecolor == '3' or linecolor == 'blue':
        linecolor = 'blue'
    elif linecolor == '4' or linecolor == 'orange':
        linecolor = 'orange'
    else:
        linecolor = 'black'

    
    pensize = random.randint(1, 5)
    tobi.pensize(pensize)
    tobi.color(linecolor,color)
    
    angle = math.sin(degrees*3.1415/180)
    tobi.lt(angle)    
    tobi.fd(1)
    degrees = degrees + 1


