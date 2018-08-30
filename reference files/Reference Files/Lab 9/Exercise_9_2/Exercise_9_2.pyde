'''Exercise 9.2  Create a txt file containing the following data on separate lines: data = 12,
67, 45, 67, 98, 33 Load the data in your program and store it in a list.
 Write a code that chooses any two random numbers from the list data and stores them
into two different variables. Use the random function
 Use the variables as parameters to your rect() function, e.g., rect(var1, var2, var1, var2).
Also use the stroke() and strokeWeight() functions.
 Modify your program such that the rectangle fill is black when the count of your draw
window is even and white if the count is odd. Your draw() should keep drawing rectangles
until you close your program. Sketch 9.4.1 is what your program should look like.
'''



def setup():
    size(200,200)
count = 0    
def draw(): 
    frameRate(10)   
    global count
    data = [12,67,45,87,90,45,67,98,33]
    var1 = data [int(random (0, len(data) ) )] 
    var2 =  data [int(random (0, len(data) ) )] 
    if count %2 == 1:
        stroke(var1)
        strokeWeight(10)
        fill(255)
        rect(var1, var2, var2, var1)
    else:
        stroke(var2)
        strokeWeight(10)
        fill(0)
        rect(var1, var2, var1, var2)
    count = count + 1
    