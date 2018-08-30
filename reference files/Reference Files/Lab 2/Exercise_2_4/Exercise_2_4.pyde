'''Exercise 2.4 Write a program that generates random numbers(integers only in the range
(0,100) and prints if the number is divisible by 5 or not. For example, if the number generated is
26, then the console should display:
26 is not divisible by 5'''

def setup():
    size(400, 500)

def draw():
    x = int(random(0, 100))
    if x % 5 == 0:
        print(x, "is divisible by 5")
    else:
        print(x, "i is not divisible by 5")