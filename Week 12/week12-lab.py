#In this lab we are going to review the topics.


# Exercise-1
# The recursive function is a concept where function is defined by itself
# that is the function body uses the function itself
# for example factorial of a number can be obtain through resursion
# 5! = 5x4x3x2x1 = 120


def myfactorial(n):
    pass

#print(myfactorial(5))  will produce 120



################# while loop ####################

# Exersice-2:
# syntax for a while loop is as follows
#
# while (cond):
#     statement 1    1
#     statement 2
#     ....
#     ...


# write a function to ask the user to input temperature of every day of a week one by one
# and print the average temperature

def avgweektemp():
    pass

# average temperature of a week if the daily temperatures are 10,20,10,20,10,20,10 will be 14.28
#print(avgweektemp()) will produce 14.28

############################### for loop ########################################


#A basic for loop that prints the value of an iterator is

# for i in range(10):
# 	print(i)

# Exercise 3:
names = ['Aala','Fiha','Maha','Arshia','Alina','Hamza','Naveen']
# print the invitation to a party for these guest one by one on the screen

def myinvitation():
    pass

# myinvitation() must produce
#
# Aala Please come to a party on Saturday.
# Fiha Please come to a party on Saturday.
# Maha Please come to a party on Saturday.
# Arshia Please come to a party on Saturday.
# Alina Please come to a party on Saturday.
# Hamza Please come to a party on Saturday.
# Naveen Please come to a party on Saturday.


# Exersice-4:
# write a function that takes a alpha numeric string and only return the digits in that string

def returndigit(mystr):
    pass

# print(returndigit('My cell number is 03335552221'))
# 03335552221

###################################################################

# Exersice-5:
# write a function which reads a file and creat a new file having the same content
# but every line starts with a line No.

def putlineNo(filename):
    pass

# putlineNo('sonnet_18.txt') will create a file name 'lineNo-sonnet_18.txt' in the
# current folder whos contents are

# Line-1:                             Sonnet 18
# Line-2:
# Line-3:               Shall I compare thee to a summer's day?
# Line-4:               Thou art more lovely and more temperate:
# Line-5:               Rough winds do shake the darling buds of May,
# Line-6:               And summer's lease hath all too short a date:
# Line-7:               Sometime too hot the eye of heaven shines,
# Line-8:               And often is his gold complexion dimm'd;
# Line-9:               And every fair from fair sometime declines,
# Line-10:               By chance, or nature's changing course, untrimm'd;
# Line-11:               But thy eternal summer shall not fade
# Line-12:               Nor lose possession of that fair thou ow'st;
# Line-13:               Nor shall Death brag thou wander'st in his shade,
# Line-14:               When in eternal lines to time thou grow'st;
# Line-15:                 So long as men can breathe or eyes can see,
# Line-16:                 So long lives this, and this gives life to thee.
# Line-17:
# Line-18:                                          -- William Shakespeare


####################################################################################
############################ HOME WORK #############################################
###################################################################################

# Exersice-1:
# write a recursive function to obtain a sum of numbers in a nested list

L = [1,[2,3],[4,5],6,7,8,[9]]

def mylistsum(L):
    pass


#print(mylistsum(L))  will produce 45


# Exercise 2:
# write a function to get n+1 sequence as a list in such a way that if n become even print n/2 in a sequence
# and if n becomes odd print n+1 in a sequence until n becomes 1 at which the function must terminate

def seqnp1(n):
    pass


# print(seqnp1(200)) will produce
# [200, 100, 50, 25, 26, 13, 14, 7, 8, 4, 2]


# Exercise-3
# write a function which takes a list of names and return a list of names starting with a specific character

def extractnames(L,ch):
    pass

# print(extractnames(names,'A')) will produce
# ['Aala', 'Arshia', 'Alina']


#Exercise-4
# write a function that takes a word and convert it into a nested list of its characters
# and the corresponsing position in the alphabets

def charNpos(mystr):
    pass


# print(charNpos('sarim')) must produce
# [['s', 19], ['a', 1], ['r', 18], ['i', 9], ['m', 13]]

# Exercise-5
# write a function which reverses every two consecutive characters in given string, if the length of the string
# is odd the last character is reversed with a space

def reversechar(mystr):
    pass

#print(reversechar('my name is sarim')) will produce
#  'ymn ma esis rami'
#print(reversechar('my name is sarims')) will produce
# 'ymn ma esis rami s'

#Exercise-6

# write a function that return (not print) the summary of a file, that is the number of lines,
# the number of words and the number of characters in the file

def filesummary(filename):
    pass

#print(filesummary('sonnet_18.txt')) #will produce
#   The file summary
#   Lines: 18
#   Words: 119
#   Characters: 926