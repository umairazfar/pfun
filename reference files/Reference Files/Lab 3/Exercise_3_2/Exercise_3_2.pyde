'''Exercise 3.5 Using nested loops fill your entire processing window with the polka dot pattern.
Also give colors to your window and the dots. You may use the point() function or the ellipse()
function to get the desired output.
'''

def setup(): 
  size(500,500)

def draw(): 
    background(113, 45, 68)
    for y in range(10, 500, 20): 
        for x in range (10, 500, 20): 
            fill(x, y, x)
            ellipse(x, y,10,10)