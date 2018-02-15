#This is a sample quiz

import os

#variables for storing User data
firstName = ""
lastName = ""
id = ""

proceed = False

while proceed == False:
    print("Please enter your information:")
    firstName = input("Enter your first name:")
    lastName = input("Enter your last name:")
    id = input("Enter your id:")

    correct = True

    while correct:
        print("\n-- Student Information --")
        print("First Name:", firstName)
        print("Last Name:", lastName)
        print("id:", id)
        print("\nIs this information correct?")
        while True:
            ans = input("Please respond in 'y' or 'n'\n")
            if ans == 'y':
                correct = False
                proceed = True
                break
            elif ans == 'n':
                correct = False
                break

filename = firstName+lastName+'.txt'
questions = []
answers = ""
string = ""

for file in os.listdir("questions"):
    if file.endswith(".txt"):
        questions.append(file)

for file in questions:
    f = open("questions\\"+file)
    string = f.read()
    print(string)
    while True:
        ans = input("Please enter your answer as a, b, c or d:")
        print("Are you sure that " + str(ans) + " is your answer?")
        sure = input("Please respond in 'y' or 'n'\n")
        if sure == 'y':
            answers = answers + ans + "\n"
            break
    f.close()

f = open(filename, "w")
f.write(answers)
f.write("END\n")
f.write(firstName + "\n")
f.write(lastName + "\n")
f.write(id)
f.close()

print(answers)