# This lab is about tuples, they are used to group things together specially when they
# are logically belong to a thing, e.g. student record. similar to list they are
# comma separated entries but unlike list they are enclosed in parenthesis
# (not a requirement but a good practice)

sam = ('Sam','1998',20,'Habib University','social science')
pam = 'Pam','1997',21,'Habib University', 'Science'

#print(type(sam),type(pam)) # will print
# <class 'tuple'> <class 'tuple'>


# similar to string tuples are immutable, we can index them similar to string. Each entry
# in a tuple is called an element.

#print(sam[0])# will print Sam
#print(pam[1]) # will print 1997

# since tuples are immutable we can not do item assignment like we do in list.
# To change entries in a tuple we have to reassign the whole tuple
# if we have only single value in tuple we have to put ',' at the end e.g (10,)
sam = sam[:3] + ('s12345',) +sam[3:]
#print(sam)

# Exercise-1:
# write a function that ask the user to provide the name as input and
# then the name of courses taken in the current semester one by one and build a
# tuple in loop having first entry as name and then the courses name.
# The loop breaks when the user inputs done.

def studentcourses():
    pass

#print(studentcourses())
#  if the name provided is Ahmed and courses are maths, physics
# then output is
#('Ahmed', 'maths', 'physics')


# Tuples can hold different data types
tam = ('Tam',20,['maths','Physics','Electronics'])
#print(tam)

# Exercise-2
# Modify the above function such that the second element of a tuple is a
# list of courses taken in the current semester in the same fashion through
# input from the user

def studentcourses2():
    pass



#print(studentcourses2())
#  if the name provided is Ahmed and courses are maths, physics
# then output is
# ('sarim', ['maths', 'physics'])


# Tuple assigment is a powerful approach where the elements in a tuple
# can be assigned to different variables in just one go

#stucour = studentcourses2()
#
# (name,courses) = stucour
#
# print(name) # prints the name of the student provided through the input
# print(courses) # prints the courses of the student provided through the input

# Exercise:3
# write a function that takes the student record  and drop the given course
# from the list if it is there and return the modified tuple

stucour = ('Sam',['Physics','Maths','Electronics'])
def dropcourse(stucour,course):
    pass

#print(dropcourse(stucour,'Maths')) # will print
# ('Sam', ['Physics', 'Electronics'])

# Exercise:4
# write a function that takes the student record  and drop the given course
# from the list if it is there and return the modified tuple

stucour = ('Sam',['Physics','Maths','Electronics'])
def addcourse(stucour,course):
    pass

#print(addcourse(stucour,'Stats')) # will print
# ('Sam', ['Physics','Maths', 'Electronics','Stats'])

# Exercise-5
# write a function that takes a student record tuple having
# name and list of courses and print the name and taken courses on the same line as
# if student course tuple is ('Sam',['Physics','Maths','Statistics'])
# then the output must be "Sam is taking Physics, Maths and Statistics"

def prtstcourserecord(stdcour):
    pass



#stdcour = ('Sam',['Physics','Maths','Electronics'])
#prtstcourserecord(stdcour) # will print
# "Sam is taking Physics, Maths and Electronics"

# Exercise-6
# write a function using studentcourses2() to form
# multiple student records as nested tuples

def studentrecords():
    pass

#print(studentrecords())


########################### HOMEWORK ########################

# Exercise-1:
# write a function that takes tutple of nested student course tuple e.g.
# studentrecords = (('Sam',['Phy','Maths','Stats']),('Pam',['Phy','Maths','chem']),...)
# and the "name" of the student whose course record needs to be modified and
# display the course list of that student and ask the user to "add" or "remove" a
# course from the student course list and return the modified students records.
# This function must call the functions already defined above

mystudentrecords = (('Sam',['Phy','Maths','Stats']),('Pam',['Phy','Maths','chem']))
def modifystdrecords(studentrecords,name):
    pass



#print(modifystdrecords(mystudentrecords,'Sam'))

# Exercise-2
# write a function which writes nested student course tuples in studentrecords to a file
# where every line is a student course tuple

def writestdrecordstofile(mystudentrecords,filename):
    pass

#writestdrecordstofile(mystudentrecords,'student-records.txt')
# will make a file whose lines are
#('Sam', ['Phy', 'Maths', 'Stats'])
#('Pam', ['Phy', 'Maths', 'chem'])

# Exercise-3
# write a function which reads student course tuples in studentrecords from a file
# where every line is a student course tuple and form a nested student course
# tuple records like
# mystudentrecords = (('Sam',['Phy','Maths','Stats']),('Pam',['Phy','Maths','chem']))

def readstdrecordsfromfile(filename):
    pass



# if the file student-records.txt contain
#('Sam', ['Phy', 'Maths', 'Stats'])
#('Pam', ['Phy', 'Maths', 'chem'])

#print(readstdrecordsfromfile('student-records.txt')) # will produce
#(('Sam', ['Phy', 'Maths', 'Stats']), ('Pam', ['Phy', 'Maths', 'chem']))
