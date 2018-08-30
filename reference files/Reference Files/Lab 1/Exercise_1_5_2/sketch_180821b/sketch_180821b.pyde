'''2. For the same window, draw a circle and give it a red color. Draw a rectangle inside the circle
and give it a different color from that of the background and the circle using RGB values.
'''

def setup():
    
    size(250,500) #window size
    
    background(32, 138, 122)  #Seagreen

def draw():
    
    fill(187, 9, 13)
    ellipse(125.5, 250, 125.5, 125.5)
    
    fill(252, 114, 135)
    rect(80, 205, 90, 87)