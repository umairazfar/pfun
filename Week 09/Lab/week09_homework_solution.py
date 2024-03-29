# Exercise 1:
# Write a function that counts and returns the number of
# non-blank lines in a given text file.
#
# Note: blank lines may contain whitespace characters (spaces,
# tabs, new lines).

def non_blank_line_count(filename):
    f = open(filename)
    c = 0
    for line in f:
        if line.strip():
            c += 1
    f.close()
    return c

# Sample output:
print(non_blank_line_count("we_real_cool.txt"))
# -> 11



# Exercise 2:
# Write a function that reads in a text file that contains
# a poem. First line of the file will contain the poem's title.
# Second line will be blank. Poem's first verse begins at line 3.
# The poem will contain at least one line in verse.
#
# Print the poem, first in the right order (including the title),
# and then in reverse order, beginning with a blank line, then
# the second-to-last line all the way up to the first line of
# the first verse.
#
# Note: when printing in reverse, do not print the last line,
# the title line, or the blank line following it.

def reverse_poem(filename):
    f = open(filename)
    reversed_poem = ''
    last_line = ''
    c = 0
    for line in f:
        print(line, end='')
        c += 1
        if c > 2:
            reversed_poem = last_line + reversed_poem
            last_line = line
    print()
    print(reversed_poem, end='')
    f.close()

# Sample output:
reverse_poem('the_lost_generation.txt')
# ->         The Lost Generation -- Jonathan Reed
# ->
# -> I am part of a lost generation.
# -> And I refuse to believe that
# -> ...
# -> It is foolish to presume that
# -> There is hope.
# -> And all of this will come true unless we choose to reverse it
# ->
# -> There is hope.
# -> It is foolish to presume that
# -> ...
# -> And I refuse to believe that
# -> I am part of a lost generation.



# Exercise 3:
# Write a function that reads in a text file, replaces all
# occurrences of one word with another, and then stores the
# resulting text in another text file.
#
# Note: words may consist of alphabets, numerals and the
# apostrophe; this task is complicated by the fact that a word
# may be a substring of another word and, in that case, must NOT
# be replaced.
#
# For example, when replacing the word "we" with "I",
# the original sentence, "I guess, well, we must be going."
# becomes "I guess, well, I must be going." even though the
# word "well" begins with "we"--that substring should NOT be
# replaced with the string "I".
#
# In essence, using str.replace method without some thoughtful
# consideration may not give the desired result.

def is_part_of_word(letter):
    return 'A' <= letter <= 'Z' or 'a' <= letter <= 'z' or '0' <= letter <= '9' or letter == "'"

def replace_word(in_filename, out_filename, old_word, new_word):
    f = open(in_filename)
    changed_text = ''
    for line in f:
        look_from = 0
        while True:
            found_at = line.find(old_word, look_from)
            if found_at == -1:
                changed_text += line[look_from:]
                break
            changed_text += line[look_from:found_at]
            # NOTE: I have deliberately left out testing if
            # found_at > 0. This is because if found_at == 0,
            # then char_before will be the last character in
            # line, which is '\n'. This would pass not pass the
            # first check in the subsequent if statement, which
            # is the desired outcome. Similar argument applies to
            # testing if found_at + len(old_word) < len(line).
            char_before = line[found_at - 1]
            char_after = line[found_at + len(old_word)]
            if is_part_of_word(char_before) or is_part_of_word(char_after):
                changed_text += old_word
            else:
                changed_text += new_word
            look_from = found_at + len(old_word)
    f.close()
    f = open(out_filename, 'w')
    f.write(changed_text)
    f.close()

# Sample output:
replace_word('we_real_cool.txt', 'i_real_cool.txt', "We", "I")
# file contents of 'i_real_cool.txt':
# -> ...
# ->             Lurk late. I
# ->             Strike straight. I
# -> 
# ->             Sing sin. I
# ->             Thin gin. I
# -> ...
replace_word('the_lost_generation.txt', 'the_lost_generation_in_of.txt', "in", "of")
# file contents of 'the_lost_generation_in_of.txt':
# -> ...
# -> So of thirty years, I will tell my children
# -> They are not the most important thing of my life.
# -> ...
