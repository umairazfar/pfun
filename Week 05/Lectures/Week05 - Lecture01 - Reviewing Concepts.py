#This lecture, we will review what we have done so far and make somethign useful

#The course breakup is given as follows:

#30% labs
#36% quizzes
#7% project 1
#12% project 2
#15% final

#We define the variables of things to calculate

labs = 0
quizzes = 0
project1 = 0
project2 = 0
final = 0
total_marks = 0

lab_marks = 150
quiz_marks = 36
    

def TotalMarks():
    name = input("Enter your name: ")
    num = int(input("Enter lab marks: "))
    labs = num/lab_marks * 30
    num = int(input("Enter Quizzes marks: "))
    quizzes = num/quiz_marks * 36
    num = int(input("Enter Project 1 marks: "))
    project1 = num/100 * 7
    num = int(input("Enter Project 2 marks: "))
    project2 = num/100 * 12
    num = int(input("Enter Final marks: "))
    final = num/100 * 15
    total_marks = labs + quizzes + project1 + project2 + final
    print("Your total marks are:", total_marks)

    if total_marks >=90:
        print("A")
    elif total_marks >=80 and total_marks <90:
        print("B")
    elif total_marks >=70 and total_marks <80:
        print("C")
    elif total_marks >=60 and total_marks <70:
        print("D")
    else:
        print("F")

TotalMarks()
print("Your total marks are:", total_marks)
#Explain local and global variables


#Change this code to assign grades
#put this on repeat till the user chooses not to enter again
