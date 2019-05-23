##
d = {0:0, 'b':1, 'c':2}
t = d.items()
print(t)
##
###printing the tuples
##for tup in t:
##    print(tup)
##
###printing keys and values separately
##for key, value in t:
##    print(key, value)

#We can create a dictionary out of tuples
##t = [('a', 0), ('c', 2), ('b', 1)]
##d = dict(t)
##print(d)


#Creating a dictionary from a zip object
#d = dict(zip('abc', range(3)))
#print(d)
##
#Creating a directory
##tup = 'Khan', 'Umair'
##directory = dict()
##directory['Khan', 'Umair'] = '0201-99887766'
##directory['Ahmad', 'Jalal'] = '0201-99887760'
##directory['Connor', 'Sarah'] = '0201-99887776'
##
##print(directory)
##
##for last, first in directory:
##    print(first, last, directory[last,first])


#Problem 1: using dictionary and tuple in file reading



##file = open('directory.txt', 'r')
##lst = file.readlines()
##print(lst)
##code=ord('a')
##code = code+3
##data = chr(code)
##print(data)
##
##code = code - 3
##data = chr(code)
##print(data)
##
##for i in range(len(lst)):
##    lst[i] = lst[i].strip()
##print(lst)
##
##direct = dict()
##for i in lst:
##    temp = i.split()
##    direct[temp[0], temp[1]] = temp[2]
##
##for tup in direct:
##    print(tup, direct[tup])


##
##
##    
##
#Problem 2:  path traversal



path = "--o--x-"

lst = list(path)
print(lst)

for i in range(len(lst)):
    if lst[i+1] == 'x':
        lst[i], lst[i+1] = lst[i+1], lst[i]
        lst[i] = '-'
        break
    if lst[i+1] == '-':
        lst[i], lst[i+1] = lst[i+1], lst[i]
        
    print(lst)
print(lst)

path = "".join(lst)
print(path)

