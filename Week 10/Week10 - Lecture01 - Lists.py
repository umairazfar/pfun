#Testing out Lists and Explaining Classes
students = ['dave', 'jim', 'carl', 'charlie', 'april']
##print (students)
##print (students[1])
##print (students[2:4])
##print (students[::2])
##print (students[1:4:2])

##for i in range(0, len(students)):
##    print(students[i])


##students.append('dave')
##print(students)
##students.remove('dave')
##print(students)
##
##
##for text in [1,2,3, 'yo']:
##    print(text)
##
numbers  = [2,5,4,6,[1,2,3]]

##numbers.sort()
##print(numbers)
##
##students.extend(numbers)
##print(students)

##print(numbers)
##
##print(numbers.pop())
##
##print(numbers)
##
##print(numbers.remove(2))
##print(numbers)
##
lst = []

file = open('data.txt', 'r')    #open a file
lst = file.readlines()              #reading lines into a list
file.close()                        #closing the file

print(lst)
 
#We see that every line is ending with a '\n' character. 
#This is a value that we do not want and we want it stripped out. 
#To do that, we write the following code:

lst=[]

file = open('data.txt', 'r')    #open a file
for line in file:
    lst.append(line.strip())        #strip the unwanted \n
file.close()                        #closing the file

print(lst)

