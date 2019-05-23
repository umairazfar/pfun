#The r operator
##print('good bye and\ngood luck')
##print(r'good bye and\n good luck')
##print(R'good bye and\n good luck')
##
###the in operator
text = 'Hello'
##print('a' in text)
##print('H' in text)
##print('h' in text)

#The not in operator
##print('a' not in text)
##print('H' not in text)
##print('h' not in text)
##
###Triple quotes
##single_line = "Obiwan: Hello there!\nGeneral Grievous: General Kenobi"
##multi_line = """Obiwan: Hello there!
##General Grievous: General Kenobi"""
##
##print(single_line)
##print(multi_line)

###*********Built-in String Functions**********
text = 'this will be a test string'
##print(text.capitalize())
##
##print(text.center(40, '*'))
##
##print(text.count('i', 3, len(text)))
##
##print(text.count('test', 0, len(text)))
##
##print(text.find('test', 0, len(text)))

#isdigit()
##print(text.isdigit())
##
##num = '233'
##
##print(num.isdigit())
##
##new_num = '233a'
##
##print(new_num.isdigit())

#isalpha()
##print(text.isalpha())
##
##num = '233'
##
##print(num.isalpha())
##
##new_num = '233a'
##
##print(new_num.isalpha())
##
##alpha = 'abcd'
##
##print(alpha.isalpha())

#islower() isupper()
##print(text.islower())
##print(text.isupper())

#strip()
spaced = ' wow! I have spaces '
print(spaced)
print(spaced.strip())

#swapcase
print(spaced.swapcase())
print(spaced.swapcase().strip())

#title()
print(text.title())

###Can you program these functions yourself?
