name = "Umair"
courses = 2
total = 0

text = ""

for i in  range(0, courses):
    text = text + input("Course Name:")
    text = text + " - "
    credit = int(input("Credit Hours:"))
    text = text + str(credit)
    text = text + " - "
    text = text + input("Grade:")
    text = text + " \n"
    total = total + credit

print(text)
print (total / courses)

#The calculation of the GPA is not correct. Make it right!
    
