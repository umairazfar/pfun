'''Exercise 6.1 Write a function that takes a string and returns a new string with all the white
spaces and special characters removed. hint: Use ASCII codes to check for the special characters.
'''

def setup():
    string_alpha("KAINAT__ABBASI")
    
    1
def string_alpha(input):
    string = ''
    for i in input:
        if (65 <= ord(i)<= 91) or (98<= ord(i)<=122):
            string = string + i
    print(string)
             