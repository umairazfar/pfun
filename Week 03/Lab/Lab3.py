#Sample 1


import turtle

#User selected turtle graphics
canvas=turtle.Canvas()
tobi=turtle.Turtle()
'''
print("What shape do you want the turtle to have?\n1. turtle\n2. triangle\n3. classic")
shape = input('Your answer is: ')

if shape == '1' or shape == 'turtle':
    shape = 'turtle'
elif shape == '2' or shape == 'triangle':
    shape = 'triangle'
elif shape == '3' or shape == 'classic':
    shape = 'classic'
else:
    print("incorrect answer, setting the turtle's shape to circle")
    shape = 'circle'

tobi.shape(shape)

print("What color do you want the turtle to have?\n1. red\n2. green\n3. blue\n4. orange")
color = input('Your answer is: ')

if color == '1' or color == 'red':
    color = 'red'
elif color == '2' or color == 'green':
    color = 'green'
elif color == '3' or color == 'blue':
    color = 'blue'
elif color == '4' or color == 'orange':
    color = 'orange'
else:
    print("incorrect answer, setting the turtle's color to gray")
    color = 'gray'

print("What color do you want the turtle's line to have?\n1. red\n2. green\n3. blue\n4. orange")
linecolor = input('Your answer is: ')

if linecolor == '1' or linecolor == 'red':
    linecolor = 'red'
elif linecolor == '2' or linecolor == 'green':
    linecolor = 'green'
elif linecolor == '3' or linecolor == 'blue':
    linecolor = 'blue'
elif linecolor == '4' or linecolor == 'orange':
    linecolor = 'orange'
else:
    print("incorrect answer, setting the turtle's color to black")
    linecolor = 'black'

tobi.color(linecolor,color)

import random
pensize = random.randint(1, 5)
print('Setting the pen size to a random value of: ', end='')
print(pensize)

tobi.pensize(pensize)

tobi.speed(1)
tobi.color(linecolor,color)
tobi.fd(80)
tobi.lt(90)
tobi.fd(60)
tobi.rt(90)
tobi.fd(60)
tobi.rt(90)
tobi.fd(60)
tobi.lt(90)
tobi.fd(60)
tobi.ht()

#Class exercise
#Change the code above such that the pensize should be given by the user
#the program should check for a valid pensive
#if pensize is not valid, assign it the value 3

#Turtle Race

import turtle
import random
canvas=turtle.Canvas()
t1=turtle.Turtle()
t1.shape('turtle')
t1.color('red','blue')
t1.pensize(2)
t1.penup()
t1.goto(-300,20)
t1.pendown()

t2=turtle.Turtle()
t2.shape('turtle')
t2.color('orange','yellow')
t2.pensize(2)
t2.penup()
t2.goto(-300,0)
t2.pendown()

t3=turtle.Turtle()
t3.shape('turtle')
t3.color('green','purple')
t3.pensize(2)
t3.penup()
t3.goto(-300,-20)
t3.pendown()

step = 0

while(step < 50):
    t1.fd(random.randint(1, 10))
    t2.fd(random.randint(1, 10))
    t3.fd(random.randint(1, 10))
    step = step+1



canvas=turtle.Canvas()
tobi=turtle.Turtle()
tobi.shape('turtle')
tobi.color('red','blue')
tobi.pensize(2)
'''

#Class Exercise
#Have the race again, but this time calculate how much distance was covered
#by each turtle

import math


#Making a sin wave

tobi.hideturtle()
tobi.penup()
tobi.goto(-200,0)
tobi.rt(60)
tobi.showturtle()
tobi.pendown()
degrees = 0
while(degrees <= 720):
    angle = math.sin(degrees*3.1415/180)
    tobi.lt(angle)    
    tobi.fd(1)
    degrees = degrees + 1



#Making a spiral

tobi.hideturtle()
tobi.penup()
tobi.goto(-200,0)
tobi.rt(60)
tobi.showturtle()
tobi.pendown()
degrees = 0
while(degrees <= 20):
    angle = math.sin(degrees*3.1415/180)
    tobi.lt(degrees)    
    tobi.fd(10)
    degrees = degrees + 0.1



#Class exercise
#Change the sin wave code such that it assigns random angle values between 1 and 30 and moves forward 30 steps everytime in each step

#Homework
#Refer to the uploaded video. You need to reproduce the same using your own code
