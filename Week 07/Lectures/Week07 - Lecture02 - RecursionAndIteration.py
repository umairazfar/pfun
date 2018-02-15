#Factorial
#Factorial is a number multiplied with a previous number and so on
#so 3! means 3 x 2 x 1
#now how to do it using for loop?
##num = 1
##for i in range(5, 1, -1):
##    num = num*i
##print(num)

###Same result can be found by this code as well

##num = 1
##for i in range(1, 6):
##    num = num*i
##print(num)

#the first attempt is more in league with how the calculations are really done

#Now to achieve the same result with recursion

#Whenever working with recursion, we need to first settle the base condition
#Or the stopping condition for a function
#In this case the base condition is 1! which means 1
#lets make a function

def Factorial(n):
    if n == 1:
        return n

#Now we test it out
#print(Factorial(1))

###If we test it out with 3, it will not work
##print(Factorial(3))
##
###The steps we need to take are:
###Give the function 3
###   Give the next function 2
###       Give the next function 1 <- this will return 1 and should be multiplied with 2
##
##def Factorial(n):
##    if n == 1:
##        return n
##    else:
##        return n * Factorial(n-1)
##
###Testing it this time:
##print(Factorial(5))

#Define a function that sums up all the numbers till a certain value
##def SumOfAll(n):
##    #Add your code here
##
##print(SumOfAll(6))
##
##def Greetings(n):
##    if n<=5:
##        print('Hello')
##        n=n+1
##        Greetings(n)
##
##
##Greetings(1)

##break and continue statement

import random

while True:
    num = random.randint(0,10)
    if num > 5:
        print ('We got a big number', num)
        continue
    print ('We have a small number', num)
    if num == 0:
        break
