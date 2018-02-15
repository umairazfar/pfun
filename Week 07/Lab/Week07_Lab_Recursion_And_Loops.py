#This lab is about understanding loops and recursion. We will try to learn
#both concepts by looking at a few examples and then work with a few exercises.

#let us look at a simple for loop

for i in range(2):
    print(i)

#now compile this code

#We can see that the loop runs twice. In the beginning, the value of i is 0
#All for loops start that way by default
#The value then becomes 1 and finally since 2 will take it beyond the range
#the loop stops there
#We can safely say that 2 is the stopping condition for this loop

#With that stopping condition in mind, we look at recursion

#in recursion, the same function is called over and over again, till a stopping
#condition is met. Lets try to replicate what we did in the loop using recursion

'''
def Counter(i):
    if i == 2:      #this is the stopping condition
        return
    print(i)        #We are just printing the value of i
    Counter(i+1)    #Calling the same function again but this time adding 1 to i

Counter(0)
'''

#Now lets look at some other code to get our bearings
'''
name = "Clive Barker"
print(name)                 #printing the name
print(name[0])              #printing the first letter
print(len(name))            #printing the length of the name
print(name[len(name) - 1])  #printing the last letter
'''

'''
for i in range(5):
    print(name[i])          #Question 1: How to print the first name in one line? 5 min

for i in range(len(name)):  #prints the entire name with one letter in each line
    print(name[i])
'''

#We can see the the loop is starting from 0 and goes on to the stopping condition

#now we would like to replicate that using recursion

'''
def RecurCounter1(i):
    if i == len(name):
        return
    print(name[i])
    RecurCounter1(i+1)

RecurCounter1(0)             #Question 2: How to reverse print the name? 5 min
'''

'''
def RecurCounter2(i):
    if i < 0:
        return    
    RecurCounter2(i-1)
    print(name[i], end="")

RecurCounter2(len(name)-1)
print()
'''

#Another way of using for loop
'''
prefixes = 'JKLMNPRST'

suffix = 'ack'
for letter in prefixes:
    print(letter + suffix)
'''
#Finding a letter in string
#We now try to find a letter in a string and report its position


#letter = input("Enter a letter of your choice and press enter: ")

'''

position = ""

for i in range(len(name)):
    if name[i] == letter:
        position = position + str(i) +", "

if len(position) > 0:
    position = position[0: len(position)-2]
else:
    print("There is no letter '", letter,"' present")

print("The letter '", letter,"' is present at the following position/s: ",position, sep="")
'''

'''
position = ""

def RecurFinder(letter, position, name, i):
    if i == len(name):
        return position
    if name[i] == letter:
        position = position + str(i) + ", "
    return RecurFinder(letter, position, name, i+1)


position = RecurFinder(letter, position, name, 0)
position = position[0: len(position)-2]
print("The letter '", letter,"' is present at the following position/s: ",position, sep="")
'''
'''
import random

text = "This is some crazy text"

print(ord(' '))

for i in range(0,len(text)):
    if ord(text[i]) != 32:
        if ord(text[i]) > 96:
            if(random.randint(0,1) == 0):
                temp = ord(text[i])
                temp-=32
                print(chr(temp), end="")
            else:
                print(text[i], end="")
        else:
            print(text[i], end="")
    else:
        print(text[i], end="")
'''

#Exercise 1:

#consider the following string:

#numbers = "0213230319"

#the numbers in the string signify the english alphabets for example:
#02 represents the letter b
#13 represents the letter m

#write a code that prints these letters based on the given string

#Exercise 2:
#using the numbers string in the above exercise, write a code that
#prints all the english alphabets out but the alphabets in the
#numbers string must be capatalized

#Exercise 3:
#write a function that takes in your first name. It then removes every second
#letter from your name and stores them in a separate string.
#your shortened name is also stored in a separate string
#it then joins the two strings together

#Exercise 4:
#write another function that takes the resultant string in Exercise 3 and returns
#it to the actual name. This should work with any name. Come up with your solution
