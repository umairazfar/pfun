'''Exercise 9.3 Generate a list containing prime numbers in the range 0 - 100. In the draw funtion
generate a random number in the given range. If the number exists in your list, draw an ellipse
with the parameters of your choice. If the number does not exist in your list, append it to your list.
'''

def setup():
    size(100,100)
list1 = []
def draw():
    count = True
    x = int(random(0,100))
    for i in range(2,10):
        if x%i == 0:
            count = False
            break
        
    if count == True:
        if x not in list1:
            list1.append(x)
        else:
            fill(x)
            ellipse(x, x, 30, 30)
    print(list1)
    
            
        
    