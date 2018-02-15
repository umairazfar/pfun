#input num 1

#input num 2

#print the menu

#input user choice

#do calculation

#print ans

#print whether you want to continue

#input user choice

#repeat or quit
def Add():
    ans = num1 + num2
    print (ans)

def Sub():
    ans = num1 - num2
    print (ans)

def Mul():
    ans = num1 * num2
    print (ans)

def Div():
    ans = num1 / num2
    print (ans)

choice = 'Yes'  #our choice is 'Yes' by default

while(choice == 'Yes' or choice == 'yes'):  #the user can enter these two ways
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))

    print("****Menu****")
    print("1.\tAdd:")
    print("2.\tSub:")
    print("3.\tMul:")
    print("4.\tDiv:")
    choice = input("What is your choice: ")

    if choice == '1' or choice == 'Add': #if choice == '1' or 'Add': makes the second statement automatically true
        Add()
    elif choice == '2' or choice == 'Sub':
        Sub()
    elif choice == '3' or choice == 'Mul':
        Mul()
    elif choice == '4' or choice == 'Div':
        Div()
    else:
        print('incorrect choice')

    print("Do you want to calculate again?")
    choice = input("Ans:")  #The loop will end if the choice is not 'Yes'

