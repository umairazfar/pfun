###Dictionary store data in key:value pairs
###Suppose we want to store your name with student id, we will do it like:
##
##student = dict()
##
##student['Ahmad'] = 'aa001'
##
##print(student['Ahmad'])
##
###now we add another student
##
##student['John'] = 'jj001'
##
##print(student['Ahmad'])
##
###we can pring the entire dictionary
##
##print(student)
##
###but what is we want to see the data in a more ordered way?
##
##items = student.items()
##print(items)
##
###we can see that all the items of the dictionary are present in a list as tuples
###Now to print those tuples
##
##for tup in items:
##    print (tup)
##
###Further refining
##
##for key, value in items:
##    print(key, value)

#Now we will learn how to populate data with different constructs

#Exercise 1
#---------------------------------------------------------------------------
#Write a function UserData() which first asks the user to enter name
#it then asks the user to give marks for Math, Urdu, English and Science
#it should check if the marks are within 0 and 100. if they are not, it should
#ask the user to reenter them marks till a correct value is entered
#it should create a subject : marks tuple and put them in a list and return
#the list

def UserData():
    pass

print(UserData())
    
###Possible output
##Enter the name of the student: Haseeb
##Enter the marks of each subject
##Marks obtained for Math are: 89
##Marks obtained for Urdu are: 88
##Marks obtained for English are: 78
##Marks obtained for Science are: 905
##
##Wrong input!
##
##Marks obtained for Science are: 95
##('Haseeb', [('Math', 89), ('Urdu', 88), ('English', 78), ('Science', 95)])
##

#Exercise 2
#---------------------------------------------------------------------------
#Change the above code such that the function UserData() accepts a list of names
#As an argument

def UserData(names):
    pass

names = ['Alison', 'Victoria']
print(UserData(names))

#Possible output
##Name of student: Alison
##Enter the marks of each subject
##Marks obtained for Math are: 99
##Marks obtained for Urdu are: 100
##Marks obtained for English are: 34
##Marks obtained for Science are: 12
##Name of student: Victoria
##Enter the marks of each subject
##Marks obtained for Math are: 88
##Marks obtained for Urdu are: 73
##Marks obtained for English are: 48
##Marks obtained for Science are: 77
##{'Alison': [('Math', 99), ('Urdu', 100), ('English', 34), ('Science', 12)], 'Victoria': [('Math', 88), ('Urdu', 73), ('English', 48), ('Science', 77)]}

#Homework
#---------------------------------------------------------------------------
#Change Exercise 2 in such a way that all the names are read from the file
#'input.txt' and it then generates the file 'output.txt'. You have to use
#dictionaries where needed and the code should work with any number of names
