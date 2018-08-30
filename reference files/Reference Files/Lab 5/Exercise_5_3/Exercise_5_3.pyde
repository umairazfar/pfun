#Exercise 5.8 Rewrite example 8.4 using loops to produce the exactly same output.

def setup():
    size(100, 100)
    drawLines(5, 15)

def drawLines(x, num):
    while num > 0:
        line(x, 20, x, 80)
        x = x+5
        num = num - 1
    