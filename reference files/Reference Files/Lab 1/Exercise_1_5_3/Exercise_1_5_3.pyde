#3. Use the quad() function to construct a trapezium exactly at the center of your window.

def setup():
    size(250, 500)

def draw():
    background(130, 67, 90)
    stroke(80, 6, 43)
    strokeWeight(15)
    fill(130, 67, 90)
    quad(50, 150, 0, 350, 250, 350, 200, 150)
    strokeWeight(5)
    stroke(0)
    fill(80, 6, 43)
    quad(50, 200, 100, 335, 150, 335, 200, 200)