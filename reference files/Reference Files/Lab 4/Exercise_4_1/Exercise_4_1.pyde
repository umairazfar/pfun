#Modify example such that it draws a pair of eyes instead of a single eye. 
def setup():
    size(100, 100)
    noStroke()
def draw():
    background(204)
    eye(65, 44)
    eye(20,50)
def eye(x, y):
    fill(254)
    ellipse(x, y, 60, 60)
    fill(0)
    ellipse(x+10, y, 30, 30)
    fill(255)
    ellipse(x+16, y-5, 6, 6)