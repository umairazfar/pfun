#Exercise 9.1 Write a function to multiply the values from two lists together and return the
#result to a new array. Print the result to the console

def setup():
    size(100,100)

def draw():
    list1 = [7 ,8, 45, 23, 89, 90, 45, 32, 1]
    list2 = [8, 4, 3, 1, 6, 5, 0 ,54,78, 54]
    output = []
    for i in list1:
        for j in list2:
            stroke(i/0.5,j/2,j)
            output.append(j*i)
            line(i,j,j,i)
    print(output)
        
    