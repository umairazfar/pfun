#List continued

#in operator

lst = ['alpha', 'bravo', 'charlie']
##
##print('bravo' in lst)
##
#####We can use this information
##
##if 'bravo' in lst:
##    print('alpha ain\'t too important')
##
###list operations
##
a = [1,2,3]
b = [4,5,6]
c = a + b
##
##print(c)
##
##del c[1:5]
##print(c)
##
##print (a*3)
##
##print(sum(a))
##
##txt = 'spam'
##li = list(txt)
##
##print(li)
##d = 'something'
##li.append(d)
##print(li)
##
##strng = 'string to split'
##data = strng.split()
##print(data)
##
##data = strng.split('i')
##print(data)

name = 'Alex John Kirk'
suffix = '@st.habib.edu.pk'
name = name.lower()
lst = name.split()
print(lst)
##print(lst[0][0])
##print(lst[1][0])
##print(lst[2][0])
prefix=''
for i in range(len(lst)):
    prefix = prefix + lst[i][0]

print(prefix)
email = prefix+suffix
print(email)
