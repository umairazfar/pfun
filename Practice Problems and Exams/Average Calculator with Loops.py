num = 0
total = 0
ans = 0
count = 0

def average(total, count):
    if count == 0:
        cal = 0
        print('Average is:', cal)
        print('Avoid dividing by 0')
    else:
        cal = total/count
        print('Average is:', cal)

while True:
    print('Add a number = ')
    num = int(input())
    total = total + num
    count+=1
    print('Do you want to input another number?')
    ans = input()
    if ans == 'y':
        continue
    else:
        break


average(total, count)

