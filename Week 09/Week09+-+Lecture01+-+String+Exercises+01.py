#We have a file named names.txt and we want to create e-mail addresses from it

#We first of all, read the file and return its contents to a string

def ReadFile(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

#filename = 'names.txt'
data = ReadFile('names.txt')
#print(data) #We check here if the file was read properly

#The issue right now is that some data is capatalized some is not
#To fix this we will convert the data to lower case and then capatalize what
#we want

new_data = data.lower()

print(data)
print(new_data)

#Remember that strings are immutable, so the original data will stay the same
#unless we want to retain the original data we overwrite it as shown below

data = data.lower()

#The problem right now is that we have the text in our desired form, but there
#is a special character. One way of fixing this is to remove any character
#that is not an alphabet

#Now remeber the ord() function. We use that to define the character limits

print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(ord(' '))
print(ord('\n'))

#so any character whose order value does not lie within this range should
#be removed. We make a function for our convenience

def TextCleaner(text):
    new_text = ''   #this is the string that we will build up
    old_i = 0
    for i in range(len(text)):
        if ord(text[i]) == 10 or ord(text[i]) == 32:
            continue
        if 65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122:
            pass
        else:
            new_text = new_text + text[old_i:i]
            old_i = i+1
    new_text = new_text + text[old_i:i+1]   #We do this because we take
                                            #into account the last part of text
                                            #where there was no special character
    return(new_text)

print(TextCleaner(data))    #We can see that the output is just what we want so we store it

data = TextCleaner(data)

#We define a function for creating email addresses

def PrefixMaker(name):
    prefix = name[0] 
    for i in range(1,len(name)):
        if name[i-1] == ' ':  #We can also use ord function
            prefix = prefix + name[i]
    return prefix

def EmailsMaker(data):
    file = open('emails.txt', 'w')
    num = 0
    old_i = 0
    num_students = 100000
    for i in range(len(data)):
        if data[i] == '\n' or i == len(data) - 1:  #We can also use ord function
            count = num%num_students
            str_count = str(count)
            zeroes = '0' * (len(str(num_students)) - len(str_count))
            prefix = PrefixMaker(data[old_i: i])
            email = prefix + zeroes + str(num) + '@st.habib.edu.pk\n'
            file.write(email)
            old_i = i+1
            num+=1
    file.close()

EmailsMaker(data)

