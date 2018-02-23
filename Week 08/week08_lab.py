# Exercise 1:
# Swap the first and last letters of a word. Leave the word unchanged
# if it has fewer than two letters.

def swap_ends(word):
    pass

print(swap_ends('cyril'))
# => lyric
print(swap_ends('eagle'))
# => eagle
print(swap_ends('bad'))
# => dab
print(swap_ends('no'))
# => on
print(swap_ends('i'))
# => i
print(swap_ends(''))
# => empty string



# Exercise 2:
# Reverse the letters of a word.

def reverse(word):
    pass

print(reverse('paws'))
# => swap
print(reverse('stressed'))
# => desserts



# Exercise 3:
# A palindrome is a word that reads the same forward and backward.
# Write a function that returns True if the supplied word is a palindrome,
# false otherwise.

def is_palindrome(word):
    pass

print(is_palindrome('racecar'))
# => True
print(is_palindrome('madam'))
# => True
print(is_palindrome('adam'))
# => False



# Exercise 4:
# You comes after tea?
# Write a function that returns true if, starting from the left in a
# given word, the letter U appears, for the first time, after letter T.

def is_u_after_t(word):
    pass

print(is_u_after_t('institution'))
# => True
print(is_u_after_t('university'))
# => False
print(is_u_after_t('tarpaulin'))
# => True
print(is_u_after_t('naughty'))
# => False



# Exercise 5a:
# Weave the letters of a given word.

def weave(word):
    pass

print(weave('abcdef'))
# => adbecf
print(weave('1234567'))
# => 1526374



# Exercise 5b:
# Unweave the letters of a woven word.

def unweave(wword):
    pass

print(unweave('adbecf'))
# => abcdef
print(unweave('1526374'))
# => 1234567



# Exercise 6:
# Translate a given word to pig Latin.
# If the word begins with a vowel or half-vowel, add the suffix "yay";
# otherwise, move the consonant to the end of the word, followed by "ay".

def pig_latin(word):
    pass

print(pig_latin('apple'))
print(pig_latin('banana'))
print(pig_latin('latin'))
