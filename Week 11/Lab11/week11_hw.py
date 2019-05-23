# Exercise 1
# Read a text file and return a list of words in the file.

def raw_word_list(filename):
    pass

##print(raw_word_list('mytext.txt'))
### -> ['I', 'am', 'Sam.', 'Sam', 'I', 'am.', 'Would', 'you', 'like', 'to', 'eat', 'pizza?', 'Yes,', 'last', 'time', 'it', 'was', 'so', 'yummy!']



# Exercise 2
# Read a text file and return a list of words without punctuation
# marks. Note: punctuation marks optionally appear at the end
# of a word.

def word_list(filename):
    pass

##print(word_list('mytext.txt'))
### -> ['I', 'am', 'Sam', 'Sam', 'I', 'am', 'Would', 'you', 'like', 'to', 'eat', 'pizza', 'Yes', 'last', 'time', 'it', 'was', 'so', 'yummy']



# Exercise 3
# Read a text file and form nested lists, one for each line,
# containing the line number and the number of words in that
# line.

def line_number_word_count_pairs(filename):
    pass

##print(line_number_word_count_pairs('mytext.txt'))
### -> [[1, 3], [2, 3], [3, 6], [4, 7]]



# Exercise 4
# Read a text file and obtain a nested list containing words and
# their corresponding length.

def raw_word_length_pairs(filename):
    pass

##print(raw_word_length_pairs('mytext.txt'))
### -> [['I', 1], ['am', 2], ['Sam.', 4], ['Sam', 3], ['I', 1], ['am.', 3], ['Would', 5], ['you', 3], ['like', 4], ['to', 2], ['eat', 3], ['pizza?', 6], ['Yes,', 4], ['last', 4], ['time', 4], ['it', 2], ['was', 3], ['so', 2], ['yummy!', 6]]



# Exercise 5
# Read a text file and obtain a nested list containing words and
# their corresponding length without punctuation mark.

def word_length_pairs(filename):
    pass

##print(word_length_pairs('mytext.txt'))
### -> [['I', 1], ['am', 2], ['Sam', 3], ['Sam', 3], ['I', 1], ['am', 2], ['Would', 5], ['you', 3], ['like', 4], ['to', 2], ['eat', 3], ['pizza', 5], ['Yes', 3], ['last', 4], ['time', 4], ['it', 2], ['was', 3], ['so', 2], ['yummy', 5]]



# Exercise 6
# Read a text file and obtain a list of only capitalized words.

def capitalized_word_list(filename):
    pass

##print(capitalized_word_list('mytext.txt'))
### -> ['I', 'Sam.', 'Sam', 'I', 'Would', 'Yes,']



# Exercise 7
# Read a text file and obtain a list of all words that end a
# sentence. Note: sentences end with a period, a question mark
# or an exclamation mark.

def raw_terminal_word_list(filename):
    pass

##print(raw_terminal_word_list('mytext.txt'))
### -> ['Sam.', 'am.', 'pizza?', 'yummy!']



# Exercise 8
# Modify the above function to obtain a list of all words,
# excluding punctuation marks, that end a sentence.

def terminal_word_list(filename):
    pass

##print(terminal_word_list('mytext.txt'))
### -> ['Sam', 'am', 'pizza', 'yummy']

# Alternative:

def terminal_word_list(filename):
    pass

##print(terminal_word_list('mytext.txt'))
### -> ['Sam', 'am', 'pizza', 'yummy']



# Exercise 9
# Write a function to obtain a list of sorted, unique words in a
# text file.

def raw_unique_sorted_word_list(filename):
    pass

##print(raw_unique_sorted_word_list('mytext.txt'))
### -> ['I', 'Sam', 'Sam.', 'Would', 'Yes,', 'am', 'am.', 'eat', 'it', 'last', 'like', 'pizza?', 'so', 'time', 'to', 'was', 'you', 'yummy!']



# Exercise 10
# Modify the above function to obtain a list of sorted, unique
# words

def unique_sorted_word_list(filename):
    pass

##print(unique_sorted_word_list('mytext.txt'))
### -> ['I', 'Sam', 'Would', 'Yes', 'am', 'eat', 'it', 'last', 'like', 'pizza', 'so', 'time', 'to', 'was', 'you', 'yummy']



# Exercise 11
# Read a text file and obtain a nested list of words without
# punctuation marks and their frequency.

def word_count(filename):
    pass

##print(word_count('mytext.txt'))
### -> [['I', 2], ['Sam', 2], ['Would', 1], ['Yes', 1], ['am', 2], ['eat', 1], ['it', 1], ['last', 1], ['like', 1], ['pizza', 1], ['so', 1], ['time', 1], ['to', 1], ['was', 1], ['you', 1], ['yummy', 1]]
