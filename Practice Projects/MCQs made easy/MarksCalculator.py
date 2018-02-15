import os

def MarksCalculator(format):
    answerFiles = []
    solution = []
    answers = []
    results = ""
    fileCount = 0

    #store all the solution answers in 'solution' list
    solutionFile = open("solution.txt", "r")
    for line in solutionFile:
        solution.append(line.strip('\n'))
    solutionFile.close()

    #store the names of all the answer files in 'answerFiles' list
    for file in os.listdir("answers"):
        if file.endswith(".txt"):
            answerFiles.append(file)

    #Open the file that will keep the final scores
    if format == "txt":
        endFile = open("scores.txt", "w")
    elif format == "xls" or format == "xlsx":
        endFile = open("scores.xls", "w")

    #for every name of file in answerFiles
    for file in answerFiles:
        score = 0
        name = "answers\\"+file
        f = open(name, "r") #Open the appropriate file
        for line in f:
            answers.append(line.strip('\n')) #At every line, remove the new line character and then append the answer
        print(answers)
        i = 0
        while answers[i] != "END": #keep traversing till END is reached
            if answers[i] == solution[i]:
                score = score + 1
            i+=1
        if format == "txt":
            finalString = "The total score of " + answers[len(answers)-3] + " " + answers[len(answers)-2] + ", Student ID: " + answers[len(answers)-1] + " is " + str(score) + "\n"
        elif format == "xls" or format == "xlsx":
            finalString = answers[len(answers) - 3] + "\t" + answers[len(answers) - 2] + "\t" + answers[len(answers) - 1] + "\t" + str(score) + "\n"
        endFile.write(finalString)
        answers.clear()
        f.close() #close the file

    endFile.close()#close the file that has all the scores

MarksCalculator("txt")
