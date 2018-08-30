'''Exercise 8.2 Write a function that iterates values in the list generated in the previous question
in the reverse order and takes (value + 10) as the parameter for the height and width of your
ellipse for even number of iterations and (value + 20) for odd number of iterations. Your pattern should
look like figure shown in the manual.'''

def setup():
    size(200, 200)
def draw():
    list1 = []
    list_even = []
    list_odd = []
    for i in range(0, 500):
        x = random(0,500)
        list1.append(x)
    for i in list1[::-1]:
        if i%2==0:
            ellipse(250,250,i+10, i+10)
        else:
            ellipse(250,250,i+20,i+20)