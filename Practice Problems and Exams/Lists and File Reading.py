# ---------------
# Question 1	(15 Marks)
# ---------------
# Given two lists:
#
# subjects = ['Math', 'Science', 'Urdu', 'English', 'Computers']
# marks = [100, 78, 88, 75, 95]
#
# Write a function MarksPrinter that iterates through the lists using recursion
# and shows individual scores like this:
#
# Computers 95
# English 75
# Urdu 88
# Science 78
# Math 100
#
# It should work for lists of any length

subjects = ['Math', 'Science', 'Urdu', 'English', 'Computers']
marks = [100, 78, 88, 75, 95]

def MarksPrinter(subjects, marks, number):
    if number == -1:
        return
    print(subjects[number], marks[number])
    MarksPrinter(subjects, marks, number-1)

MarksPrinter(subjects, marks, len(subjects)-1)


# ---------------
# Question 2	(15 Marks)
# ---------------
#
# in order to get value of sin and cos, you need to import math file like this:
# 
# import math
# print (math.sin(30*math.pi/180)) #for 30 degrees
#
# write a recursive function SineVales that writes all the sin values from 0 to 360 degrees
# line by line in a text file called sin.txt


import math

def SineValues(degrees, file):
    if degrees == 361:
        return
    txt =  str(math.sin(degrees*math.pi/180))
    file.write(txt + '\n')
    SineValues(degrees+1, file)

file = open("sin.txt", "w")
SineValues(0, file)
file.close()

# ---------------
# Question 3	(10 Marks)
# ---------------
#
# In question 2, you produce a file named sin.txt:
# 
# create a function Reverse that that reads from sin.txt and writes another file reverse.txt
# but prints all the values in reverse order
# for example, if there are only 3 lines in sin.txt like this:
#
# 1
# 2
# 3
#
# then reverse.txt should contain
# 3
# 2
# 1
#
# Tip: Recursion not needed

def Reverse(file):
    filer = open(file, 'r')
    txt = filer.read()
    data = txt.split('\n')
    filer.close()

    filew = open('reverse.txt', 'w')
    for i in range(len(data)):
        filew.write(data[(len(data)-1)-i] + '\n')
    filew.close()

Reverse("sin.txt")
