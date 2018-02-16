#Variable Scope
'''
def change(age):
    age = 30
    print(age)

age = 10

change(age)

print(age)
'''
#Using id() function to understand memory

'''
def change(age):
    age = 30    #Run the code with and without this line
    print(age)
    print(id(age))

age = 10

change(age)

print(age)
print(id(age))
'''

#What force should be applied to a ball of 4 kg, to make it move 5m in
#2 seconds from an initial position of rest
'''
initVel = 0
time = 2
distance = 5
mass = 4
acc = 0
force = 0

def getAcceleration(initVel = 0, time = 1, distance = 20):
    acc = 2/(time*time) * (distance - initVel * time)
    return acc

def getForce(mass, acc):
    force = mass * acc
    return force

acc = getAcceleration(initVel, time, distance)
print(getForce(mass, acc))

acc = getAcceleration(2, 5, 60)
print(getForce(mass, acc))

acc = getAcceleration()
print(getForce(mass, acc))

acc = getAcceleration(initVel = 10)
print(getForce(mass, acc))

acc = getAcceleration(time = 4, initVel = 1)
print(getForce(mass, acc))
'''
#writing and reading files
'''
f = open("testing.txt", "w")
f.write("I may be smart\nBut you are smarter!\n")
f.close()

f = open("testing.txt")
string = f.read()
f.close()
print(string)
'''
#writing a file and reading line by line
'''
f = open("testing.txt", "w")
f.write("I may be smart\nBut you are smarter!\n")
f.close()

f = open("testing.txt")
for line in f:
    print(line)
f.close()
'''
