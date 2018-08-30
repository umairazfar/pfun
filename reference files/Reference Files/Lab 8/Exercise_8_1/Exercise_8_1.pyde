'''Exercise 8.1 Using loops generate a list containing numbers in the range (0,500). Split the odd
and even numbers into two different lists.
'''


list1 = []
list_even = []
list_odd = []
for i in range(0, 500):
    x = int(random(0,500))
    list1.append(x)
for i in list1:
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list1)
print(list_even)
print(list_odd)