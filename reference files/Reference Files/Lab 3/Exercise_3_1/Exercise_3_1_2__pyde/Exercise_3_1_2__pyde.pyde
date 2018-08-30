def setup():
    size(500, 500)
    
count = 0
c = 0
x = 0
def draw():
    global count 
    global c
    global x
    frameRate(3)
    for i in range(700, 1, -5):
        if count % 2 ==0:
            fill(0)
            ellipse(250, 250, i, i)
        else:
            fill(255)
            ellipse(250, 250, i, i)
        count = count + 1
    # Extra  
    '''
    frameRate(10);
    if (c%2==0):
        fill(0);
        ellipse(250,250,x,x)
    else:
        fill(255)
        ellipse(250,250,x,x)
    x=x+10
    c=c+3
    '''