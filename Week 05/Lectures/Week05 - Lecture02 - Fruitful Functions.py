def Add():
    print(10 + 20)

Add()   #this will print the sum

def Add():
    sum = 10 + 20
    return sum

value = Add()   #this will return the value of some which will be stored
print(50 + value)

def Multiple(num, power):
    ans = num**power
    return ans

number = int(input("Enter a number: "))
pow1 = int(input("Enter a power: "))
print(Multiple(number, pow1))
