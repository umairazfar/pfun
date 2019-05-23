#Identical Objects
a = 'banana'
b = 'banana'
if b is a:
    print(True)
else:
    print(False)
#In this example, Python only created one string object,
#and both a and b refer to it. But when you create two lists,
#you get two objects:

##a = [1, 2, 3]
##b = [1, 2, 3]
##if b is a:
##    print(True)
##else:
##    print(False)
##
###This is mainly because a string is immutable so it makes
###more sense to make one object and let all the variables
###point to it
##    
###Now if a refers to an object and you assign b = a,
###then both variables refer to the same object:
##
##a = [1, 2, 3]
##b = a
##if b is a:
##    print(True)
##else:
##    print(False)
##
###We need to be careful when a list is passed as an argument
###and when a string is passed as as argument to a function
##
##def ChangingString(text):
##    myText = text
##    myText = 'Better'
##
##def ChangingList(lst):
##    myList = lst
##    myList.append('Better')
##
##text = 'Good'
##lst = ['Good']
##
##ChangingString(text)
##ChangingList(lst)
##
##print(text)
##print(lst)
###Sorting

num = [9, 1, 4, 2]

#how can we sort this list?
#We make a simple algorithm, we compare two numbers,
#if one number is greater than the other, we swap them
#we do this manually first

if num[0] > num[1]:
    temp = num[0]
    num[0] = num[1]
    num[1] = temp

#We check our result
print(num)

#We get [1, 9, 4, 2]
#We need to do this again, but for the next values

if num[1] > num[2]:
    temp = num[1]
    num[1] = num[2]
    num[2] = temp

#We check our result
print(num)

#We get [1, 4, 9, 2]
#We need to do this again, but for the next values

if num[2] > num[3]:
    temp = num[2]
    num[2] = num[3]
    num[3] = temp

#We check our result
print(num)

#We get [1, 4, 2, 9]
#We can see that it is a bit sorted but still not perfect
#We repeat this process again, but from the start

if num[0] > num[1]:
    temp = num[0]
    num[0] = num[1]
    num[1] = temp

#We check our result
print(num)

#We get [1, 4, 2, 9]
#We need to do this again, but for the next values

if num[1] > num[2]:
    temp = num[1]
    num[1] = num[2]
    num[2] = temp

#We check our result
print(num)

#We get [1, 2, 4, 9] which is the result
#but the computer does not know that, hence it has to go all
#the way in order to ensure
#We need to do this again, but for the next values

if num[2] > num[3]:
    temp = num[2]
    num[2] = num[3]
    num[3] = temp

#We check our result
print(num)

#We have received the result but the computer
#just performed operations
#the computer does not know if the list was already sorted
#it just followed instructions

#We can perform the same operation by using loops

num = [9, 1, 4, 2, 5, 3, 7, 6, 8]

for i in range(1,len(num)):
    for j in range(0, len(num)-1):
        if num[j] > num[i]:
            temp = num[j]
            num[j] = num[i]
            num[i] = temp

print(num)
