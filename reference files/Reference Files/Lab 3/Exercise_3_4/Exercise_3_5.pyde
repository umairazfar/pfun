'''Exercise 3.4 Modify the code in 3.10 by using the line function instead of rect() such that it
creates a smiliar visual pattern.'''


noStroke()
y=1000
for i in range(0, 100, 10):
    for j in range(0, 100, 10):
        strokeWeight(10)
        stroke((i+j) * 1.4)
        line(0, y, y, 0)
        y = y-10