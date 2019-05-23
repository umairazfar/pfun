#A dictionary is like a list, but more general.
#In a list, the indices have to be integers; in a
#dictionary they can be (almost) any type.

#A dictionary contains a collection of indices,
#which are called keys, and a collection of
#values. Each key is associated with a single value.
#The association of a key and a value is
#called a key-value pair or sometimes an item.

#In mathematical language, a dictionary represents a
#mapping from keys to values, so you can also say that
#each key “maps to” a value. As an example, we’ll build a dictionary that
#maps from English to Urdu words, so the keys and the values are all strings.

#definition
data = {}
print(data)

data = dict()
print(data)

data['one'] = 'aik'
data['two'] = 'do'
data['three'] = 'teen'
data[6] = 'roku'    #this is japanese for 6

#what we are doing here are making key:value pairs. now if we print, we get

print(data)
##
##lst = []
##lst.append(2)
##lst.append(7)
##print(lst)
##
##for value in lst:
##    print (value)
##
#We can find the length by:
##print('Length of data is:', len(data))

#We can print individual values using the key
##print(data['three'])
##
#The in operator tells us if a key exists in dictionary or not
##print('one' in data)    #returns true
##print('three' in data)     #returns false as 'do' is a value, not a key
##
###to get all the values in a dictionary as a list, we write:
all1 = data.values()
print(all1)
##
#now we can see if that value is present in the list and we will get a True
##print('do' in all1)
##
##import string
##alpha={}
##string = string.ascii_lowercase
##print(string)
##lst = list(string)
##print(lst)
##
##for i in range(len(lst)):
##    alpha[lst[i]] = i
##
##print(alpha)
##
##
##alpha ={}
##
##for i in range(97, 97+26):
##    alpha[chr(i)] = i-96
##    print(alpha[chr(i)])
##
##print(alpha)

#making a Dictionary of names from a file
file = open('names.txt', 'r')
allnames = file.readlines()
file.close()

print(allnames)

for i in range(len(allnames)):
    allnames[i] = allnames[i].split()

print(allnames)

for i in range(len(allnames)):
    allnames[i] = allnames[i][1:]

print(allnames)

names = {}

for i in range(len(allnames)):
    names[allnames[i][0]] = allnames[i][1]

print(names)

print(names['Emma'])


