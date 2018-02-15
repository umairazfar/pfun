#Write a function that prints numbers from 0 to 9 by using loops
def CounterWithIteration(n):
    #Add code here

#Write a function that prints numbers from 0 to 9 by using Recursion
def CounterWithRecursion(n):
    #Add code here

#Write a function that prints numbers from 9 to 0 by using loops
def ReverseCounterWithRecursion(n):
    #Add code here

#Write a function that searches an alphabet in a string
def SearchingAnAlphabet(alphabetToSearch, theString):
    #Add code here

#Write a function that searches an alphabet in a string and tells about its location in string
def SearchingTheAlphabetLocation(alphabetToSearch, theString):
    #Add code here

#Draw a rectangle of defined length and width but empty from inside
def Rectangle(width, height):
    #Add code here

#You should call functions like this
CounterWithIteration(0)
CounterWithRecursion(0)
ReverseCounterWithRecursion(0)
SearchingAnAlphabet('g', 'This is an incredible game')
SearchingTheAlphabetLocation('g', 'This is an incredible game')
Rectangle(6, 8)

##Two frogs named 'FrogPrime' and 'Frogatron' are in a well of depth 1000 feet. They decide to race each other to the top to see who is the winner.
##
##Both frogs can jump 4 feet at a time but slide down 1 foot every time, thus making the total distance covered to be 3 feet.
##
##FrogPrime has a 2% chance to get an adrenaline rush and jump 5 feet.
##Frogatron has special claws that have a 2% chance to grab on to a wall, thus it does not slide down 1 foot if the claws connect
##
##The frogs will keep on jumping till one of them clears the well and is declared the winner.
## 
##Your program should simulate this behavior. It should find out the winner and report it. It should also report if there is a tie.
##
##It should also display the progress of the frogs at every 50th jump.
##
##It should also display the total number of jumps once the competition is over.
##
##The output should be similar to this:
##
##Distance covered by frogPrime= 3
##Distance covered by frogatron= 3
##Distance covered by frogPrime= 159
##Distance covered by frogatron= 155
##Distance covered by frogPrime= 314
##Distance covered by frogatron= 307
##Distance covered by frogPrime= 473
##Distance covered by frogatron= 464
##Distance covered by frogPrime= 631
##Distance covered by frogatron= 630
##Distance covered by frogPrime= 798
##Distance covered by frogatron= 800
##Distance covered by frogPrime= 977
##Distance covered by frogatron= 979
##frogatron is winner
##Total jumps= 307
