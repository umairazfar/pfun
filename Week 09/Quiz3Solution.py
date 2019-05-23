#Question 1 (10 Marks)
#Write a function that counts the total number of vowels in a string.
#Make sure that the returned string is exactly like the sample output
def VowelCounter(text):
    count = 0
    for letter in text:
        if letter in 'aeiou':
            count+=1

    return 'The total number of vowels are ' + str(count)

print(VowelCounter('a quick hen'))
#sample output
#The total number of vowels are 4

#Question 2 (10 Marks)
#Write a function that generates an email address using a person's first name
#and the date of birth. Make sure that the email is in lower case
def EmailMaker(name, year):
    email = name.lower() + str(year) +'@st.habib.edu.pk'
    return email

print(EmailMaker('Umair', 1989))
#sample output
#umair1989@st.habib.edu.pk

#Question 3 (10 Marks)
#Write a function that takes a string, removes all the spaces and returns
#a new string without any spaces
def Joiner(text):
    result = ''
    for i in range(len(text)):
        if text[i] is not ' ':
            result += text[i]
    return result

print (Joiner('I Can Read This Because Of Camel Casing'))
#sample output
#ICanReadThisBecauseOfCamelCasing        
