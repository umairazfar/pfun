'''Exercise 8.3 Create an empty list named list_areas. Write a function that uses random() to
generate areas of equilateral triangles and calculates the length of each side. Append the lengths
to list_areas and keep drawing a line of that length on your window.
Area of an equilateral triangle is given in the manual'''


def setup():
    size(500, 500)
list_areas = []

def draw():
    x = int(random(0,1000))
    side = int(sqrt((x*4)/sqrt(3)))
    print(side)
    list_areas.append(side)
    x2 = random(0, 500)
    x1 = random(0,500)
    y2 = random(0,500)
    y1 = random(0,500)
    lengh = int(sqrt(((x2-x1)**2) + ((y2 -y1)**2)))
    if lengh == side:
        line(x1,y1,x2,y2)
        
    