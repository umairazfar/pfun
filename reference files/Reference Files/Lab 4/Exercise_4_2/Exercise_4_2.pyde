'''Exercise 4.2 Look up the pushMatrix() and popMatrix() function and understand their working.
Create a program and define a function named rec() which draws a series of 5 rectangles 100 units
high and 150 units wide whenever the mouse is pressed. hint: Use loops and transformations.
'''

def setup():
    size(500, 500)

def draw():
    if mousePressed:
        for i in range(0, 5):
            translate(20, 10)
            fill(mouseX, mouseY, i)
            rect(mouseX, mouseY, 100, 150)