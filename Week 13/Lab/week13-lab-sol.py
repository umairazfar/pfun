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
    name = input('Please provide your name: ')
    mytuple = (name,)
    while True:
        course = input('Please provide course name or write "done" to finish: ')
        if course == 'done':
            break
        else:
            mytuple = mytuple+(course,)

    return mytuple

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
    name = input('Please provide student name: ')
    mytuple = (name,)
    course = []
    while True:
        mycourse = input('Please provide course name or write "done" to finish: ')
        if mycourse == 'done':
            mytuple = mytuple + (course,)
            break
        else:
            course.append(mycourse)


    return mytuple

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
    (name,courses) = stucour
    if course in courses:
        courses.remove(course)

    stucour = (name,courses)
    return stucour

#print(dropcourse(stucour,'Maths')) # will print
# ('Sam', ['Physics', 'Electronics'])

# Exercise:4
# write a function that takes the student record  and drop the given course
# from the list if it is there and return the modified tuple

stucour = ('Sam',['Physics','Maths','Electronics'])
def addcourse(stucour,course):
    (name,courses) = stucour
    if course not in courses:
        courses.append(course)

    stucour = (name,courses)
    return stucour

#print(addcourse(stucour,'Stats')) # will print
# ('Sam', ['Physics','Maths', 'Electronics','Stats'])

# Exercise-5
# write a function that takes a student record tuple having
# name and list of courses and print the name and taken courses on the same line as
# if student course tuple is ('Sam',['Physics','Maths','Statistics'])
# then the output must be "Sam is taking Physics, Maths and Statistics"

def prtstcourserecord(stdcour):
    (name,courses) = stdcour
    print(name,'is taking',end=' ')
    for i in range(len(courses)):
        if i == len(courses)-1:
            print('and',courses[i],end=' ')
        elif i == len(courses)-2:
            print(courses[i],end=' ')
        else:
            print(courses[i]+',',end=' ')



#stdcour = ('Sam',['Physics','Maths','Electronics'])
#prtstcourserecord(stdcour) # will print
# "Sam is taking Physics, Maths and Electronics"

# Exercise-6
# write a function using studentcourses2() to form
# multiple student records as nested tuples

def studentrecords():
    print('Please provide student name and courses for student record')
    stdrecords = ()
    while True:
        newstdrecord = studentcourses2()
        stdrecords+= (newstdrecord,)
        yn = input('Would you like to add another record (yes/no): ')
        if yn == 'yes':
            continue
        else:
            break
    return stdrecords

#print(studentrecords())# could produce
# (('saim', ['phy', 'chem']), ('jeff', ['chem', 'stats', 'maths']))


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
    newstudentrecords = ()
    for (names,courses) in studentrecords:

        if names == name:
            stdcour = (names,courses)
            prtstcourserecord(stdcour)
            count = 0
            while True:
                cond = input('\nWould you like to add/remove a course (add/remove/cancel): ')
                if cond== 'cancel' and count==0:
                    print('No record is updated')
                    break
                elif cond== 'cancel' and count!=0:
                    print('record is updated')
                    break
                elif cond=='add':
                    mycourse = input('Please provide a course to add: ')
                    stdcour = addcourse(stdcour,mycourse)
                    prtstcourserecord(stdcour)
                    count+=1
                elif cond=='remove':
                    mycourse = input('Please provide a course to remove: ')
                    stdcour=dropcourse(stdcour,mycourse)
                    prtstcourserecord(stdcour)
                    count += 1
        else:

            stdcour = (names, courses)


        newstudentrecords += (stdcour,)
    return newstudentrecords


#print(modifystdrecords(mystudentrecords,'Pam'))




# Exercise-2
# write a function which writes nested student course tuples in studentrecords to a file
# where every line is a student course tuple

def writestdrecordstofile(mystudentrecords,filename):
    f = open(filename,'w')
    for record in mystudentrecords:
        f.write(str(record)+'\n')
    f.close()

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
    f = open(filename)
    lines = f.readlines()
    mystudentrecords = ()
    for line in lines:
        words = line.split(',')
        name = words[0]
        myname=''
        for i in name:
            if i not in ["'",'"','"','(',')']:
                myname+=i

        courses = words[1:]

        mycourse = ''
        courselist = []
        for course in courses:
            for i in course:
                if i not in [' ',"'",'(',')','[',']']:
                    mycourse += i

            courselist.append(mycourse)
            mycourse=''
        lastcourse = courselist[-1]
        courselist[-1] = lastcourse[:-1]
        stdrecord = (myname,courselist)
        mystudentrecords+= (stdrecord,)

    return (mystudentrecords)

    f.close()



# if the file student-records.txt contain
#('Sam', ['Phy', 'Maths', 'Stats'])
#('Pam', ['Phy', 'Maths', 'chem'])

#print(readstdrecordsfromfile('student-records.txt')) # will produce
#(('Sam', ['Phy', 'Maths', 'Stats']), ('Pam', ['Phy', 'Maths', 'chem']))
