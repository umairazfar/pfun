#Lab04 - Understanding Functions

import turtle

#Initializing turtle with default values
canvas=turtle.Canvas()
tobi=turtle.Turtle()
tobi.shape('turtle')
tobi.color('black','green')
tobi.pensize(5)

#Defining a function here
def MoveTurtle(distance):
    tobi.fd(distance)

#If we try to run this code without calling the function, nothing will happen

#Hence, we need to call it
MoveTurtle(50)

#uncomment the code below to call it again
#MoveTurtle(50)

#Now we write the same function, but we also tell if the tail should be up or down
def MoveTurtle(distance, tail_state):
    if tail_state == 'up':
        tobi.penup()
    else:
        tobi.pendown()
        
    tobi.fd(distance)

MoveTurtle(50, 'up')
MoveTurtle(50, 'down')
MoveTurtle(50, 'up')
MoveTurtle(50, 'down')

#This makes our life easier, but the code only works for tobi, what if we want to
#make it work for other turtles? So we make more changes

def MoveTurtle(turtle, distance, tail_state):
    if tail_state == 'up':
        turtle.penup()
    else:
        turtle.pendown()
        
    turtle.fd(distance)

#now, whatever turtle's name we give, the code will make it move
#Lets define another turtle

obito=turtle.Turtle()
obito.shape('turtle')
obito.color('red','purple')
obito.pensize(5)

MoveTurtle(obito, 100, 'down')
#Now moving tobi
MoveTurtle(tobi, 100, 'down')

#Exercise 1
#Create a function that defines the shape, color, line color and line thickness
#of a turtle

#Now we create a function by which a turtle draws a rectangle at any location

def MakeRect(turtle, x, y, line_length):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.fd(line_length)
    turtle.lt(90)
    turtle.fd(line_length)
    turtle.lt(90)
    turtle.fd(line_length)
    turtle.lt(90)
    turtle.fd(line_length)
    turtle.rt(90)

#now making tobi and obito make rectangles at different locations
MakeRect(tobi, -200, -200, 100)
MakeRect(obito, 0, -300, 50)
#and again
MakeRect(tobi, -200, 400, 30)
MakeRect(obito, 50, 100, 120)

#Exercise 2
#Change the MakeRect function in such a way that the rectangle is centered

#Exercise 3
#Even though the Function is MakeRect, it is making squares. Change it in
#such a way that it actually draws rectangles, all centered

#Exercise 4
#Write a program that creates a chessboard. Do not forget to fill the rectangles
#Use functions!

#Homework lab 04
#Look at the Picture Lab04_Homework

#You need to write a function that sets up the turtles as shown
#One turtle is green with black line
#The other turtle is black with green line

#Now this is a two player game. The aim is to hit the other turtle
#Your turtle cannot go outside the boundary, in which case the other person wins
#Your turtle cannot hit the middle wall.
#You need to move your turtle in such a way that it falls on top of the other
#turtle. If your turtle goes past it, that is not considered a kill
#Both you and your partner take turns
#The program will ask you the angle to move and the distance to cover one by one
