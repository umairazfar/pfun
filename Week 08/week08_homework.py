# Exercise 1: ROTATING A WORD
# Given a word 'grape', a rotation is found by moving one letter from
# the head to the tail of the word.
# 'grape' rotated once => 'rapeg'
# 'grape' rotated twice => 'apegr'
# 'grape' rotated thrice => 'pegra'
# Write a function named rotate with parameters s and n (str and int
# respectively) that rotates the given string s, n times.

def rotate(s, n):
    pass

print(rotate('potato', 1))
# => otatop
print(rotate('potato', 2))
# => tatopo
print(rotate('potato', 3))
# => atopot
print(rotate('potato', 0))
# => potato



# Exercise 2: ROTATING RIGHT
# In exercise 1, the given word is rotated to the left. It may also be
# rotated to the right.
# 'grape' rotated right once => 'egrap'
# 'grape' rotated right twice => 'pegra'
# 'grape' rotated right thrice => 'apegr'
# Write a function named rotate_right with parameters s and n that rotates
# the given string s, n times to the right.

def rotate_right(s, n):
    pass

print(rotate_right('potato', 1))
# => opotat
print(rotate_right('potato', 2))
# => topota
print(rotate_right('potato', 3))
# => atopot
print(rotate_right('potato', 0))
# => potato



# Exercise 3: ROTATIONALLY EQUIVALENT?
# Two words are rotationally equivalent if one of the words is a rotation
# of the other.
# Write a function named are_rot_eq with parameters s and t (two strings)
# that returns true if two strings are rotationally equivalent, false
# otherwise.

def are_rot_eq(s, t):
    pass

print(are_rot_eq('laughters', 'slaughter'))
# => True
print(are_rot_eq('laughter', 'slaughter'))
# => False
print(are_rot_eq('snap', 'naps'))
# => True
print(are_rot_eq('pans', 'span'))
# => True
print(are_rot_eq('deer', 'reed'))
# => False
print(are_rot_eq('no', 'on'))
# => True
print(are_rot_eq('a', 'a'))
# => True
print(are_rot_eq('', ''))
# => True
