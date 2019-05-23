###Tuples
##
###Declaration:
##t = 'a', 'b', 'c'
##print(t)
##
###similarly
##t = ('a', 'b', 'c')
##print(type(t))
##
###When declaring for a single value, use a comma at the end
##
##t = 'a',
##print(type(t))
##
##t = ('a',)
##print(type(t))
##
###otherwise it will take it as a string
##
##t = ('a')
##print(type(t))

#We can also create an empty tuple

##t = ()
##print(t)
##
##t = tuple()
##print(t)

#We can use the built in function in different ways

##t = tuple("This is a tuple")
##print(t)
##
##t = tuple([1,2,3,4])
##print(t)

##t = tuple(('a', 2, 'b', "Hello"))
##print(t)

#getting values

##print(t[0])
##print(t[1:3])

#tuple is immutable
##t[0] = 'Z'

#But we can make a new tuple using old tuple
##t = ('Z',) + t[1:]
##print(t)

#swapping values
##a = 10
##b = 20
##temp = a
##a = b
##b = temp
##print(a, b)

#Tuples for swapping values
##a, b = b, a
##print(a, b)
##
#number of variables on the left should be equal to the ones on right
##one, two, three = 'what.is.this?'.split('.')
##print(one, two, three)

#using divmod to get quotient and remainder

##t = divmod(11,3)
##print(t)
##
#here * is used to gather arguments
##def printall(*args):
##    print(args)
##
##printall(1,2,3,4,5)

#* can be used for scatter
#t=(6,3)
#print(divmod(*t))

#rint(divmod(*t))
##
##s = 'abc'
##t = [0, 1, 2]
##j = (9,8,0)
##k = zip(s, t, j)
##
##print(k)
##
##for pair in k:
##    print(pair)
####
####string = 'hello'
####for letter in range(len(string)):
####    print(letter)
##
##lst = list(zip(s,t))
##print(lst)
##
##lst = tuple(zip(s,t))
##print(lst)

##s = 'abcde'
##t = [0, 1, 2]
##k = zip(s, t)
##
##lst = tuple(k)
##print(lst)
##
##for pair in lst:
##    print(pair)
##
##for letter, number in lst:
##    print(letter, number)

t1 = "abcde"
t2 = "zasdg"
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False
print(has_match(t1, t2))

for index, element in enumerate('abcdefghijkl'):
    print(index, element)

##for index, element in enumerate(lst):
##    print(index, element)
##
