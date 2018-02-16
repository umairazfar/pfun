#Testing out Lists and Explaining Classes
students = ['dave', 'jim', 'carl', 'charlie', 'april']
print (students)
#print (students[1])
#print (students[2:4])
#print (students[::2])
#print (students[1:4:2])

#for i in range(0, len(students)):
#    print(students[i])


#students.append('dave')
#print(students)
#students.remove('dave')
#print(students)


#for x in [1,2,3]:
#    print(x)

#numbers  = [2,5,4,6]

#numbers.sort()

#students.extend(numbers)
#print(students)

#print(numbers)

#print(numbers.pop())

#print(numbers)

#print(numbers.remove(2))
#print(numbers)

'''
class Rectangle:
    length = 0
    width = 0
    
    def Area(self, length=30, width=70):
        self.length = length
        self.width = width
        return self.length * self.width

    def Parameter(self):
        return 2*(self.length+self.width)

r = Rectangle()
print(r.Area(10,40))

print(r.Parameter())
'''

'''
class Student:
    def setName(self):
        self.name = input("Student Name:")
    def setAge(self):
        self.age = input("Student Age:")
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

a = Student()
a.setName()
a.setAge()

b = Student()
b.setName()
b.setAge()

everyone = [a,b]

for i in range(0, len(everyone)):
    print(everyone[i].getName())
    print(everyone[i].getAge())
'''
#Write a program that takes input fro a user in a loop and then prints that in a file
