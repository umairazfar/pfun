# Common file operations
# ----------------------
#   Open a text file to read:
#       dict_file = open('dictionary.txt')
#
#   Open/create a text file to (over)write:
#       recipe_file = open('recipe.txt', 'w')
#
#   Open/create a text file to append:
#       contacts_file = open('contacts.txt', 'a')
#
#   Read the entire file as a string:
#       contents = f.read()
#
#   Read a file one line at a time:
#       for line in f:
#           print(line, end='')
#   Note: each line is terminated by a newline character,
#         which is included in the line string.
#
#  Close a file:
#      f.close()

# Common string operations
# ------------------------
#   Concatenate two string together:
#       'ek se' + ' ' + 'bhale do' == 'ek se bhale do'
#
#   Replicate a string several times:
#       'La' * 7 == 'LaLaLaLaLaLaLa'
#
#   Get the length of a string:
#       len('seven') == 5
#
#   Get the Unicode code-point of a character:
#       ord('Z') == 90
#
#   Get the corresponding character for a Unicode code-point:
#       chr(90) == 'Z'
#
#   To see whether one string is part of another string:
#       'mental' in 'Programming Fundamentals' == True
#
#   Convert a string to lowercase:
#       "It's fun to stay at the Y.M.C.A.".lower() ==
#         "it's fun to stay at the y.m.c.a."
#
#   Convert a string to uppercase:
#       "I'm not shouting!".upper() == "I'M NOT SHOUTING!"
#
#   Count the number of occurrences of a substring in a string:
#       'butterfingers'.count('er') == 2
#
#   Look for a position in a string where a substring occurs,
#   starting from the left:
#       'coconut'.find('co') == 0
#
#   Look for a position in a string where a substring occurs,
#   starting from the right:
#       'coconut'.rfind('co') == 2
#
#   Replace all occurrences of one substring with another in
#   a string:
#       'A pal in need is a pal indeed.'.replace('pal', 'friend')
#         == 'A friend in need is a friend indeed.'
#
#   Remove all white space from either end of a string:
#       '    A Tale of Two Cities    '.strip()
#         == 'A Tale of Two Cities'
#
#   Get a particular character in a string:
#       'abcdef'[0] == 'a'
#       'abcdef'[5] == 'f'
#       'abcdef'[6] -> error
#       'abcdef'[-1] == 'f'
#       'abcdef'[-6] == 'a'
#       'abcdef'[-7] -> error
#
#   Get a string slice:
#       'abcdef'[3:5] == 'de'
#       'abcdef'[5:3] == ''
#       'abcdef'[3:8] == 'def'
#       'abcdef'[3:] == 'def'
#       'abcdef'[:3] == 'abc'
#       'abcdef'[2:5:2] == 'ce'
#       'abcdef'[5:2:-1] == 'fed'
#       'abcdef'[::-2] == 'fdb'

# Exercise 1:
# Write a function that counts and returns the number of lines in
# a given text file.

def line_count(filename):
    f = open(filename)
    c = 0
    for line in f:
        c += 1
    f.close()
    return c

# Sample output:
print(line_count('we_real_cool.txt'))
# -> 16



# Exercise 2:
# Write a function that reads in each line of a text file,
# reverses its contents while preserving the white space at the
# ends, and prints out the line.

def reverse(s):
    return s[::-1]

def reverse_lines(filename):
    f = open(filename)
    for line in f:
        contents = line.strip()
        start = line.find(contents)
        end = start + len(contents)
        line = line[:start] + reverse(contents) + line[end:]
        print(line, end='')
    f.close()

# Sample output:
reverse_lines('we_real_cool.txt')
# ->            .sreyalP looP ehT
# ->       .levohS nedloG eht ta neveS
# -> ...



# Exercise 3:
# Write a function that reverses the order of lines in a file,
# then store those lines in another file.

def reverse_file(filename, reversed_filename):
    f = open(filename)
    reversed_file = ''
    for line in f:
        reversed_file = line + reversed_file
    f.close()
    f = open(reversed_filename, 'w')
    f.write(reversed_file)
    f.close()

# Sample output:
reverse_file('we_real_cool.txt', 'cool_real_we.txt')
# contents of file 'cool_real_we.txt'
# ->                -- Gwendolyn Brooks
#
# ->            Die soon.
# ->            Jazz June. We
# -> ...



# Exercise 4:
# Write a function that takes an int n as argument, generates n
# pairs of random ints between 0 and 300 inclusive, and stores
# them in a given file, one pair per line, with one space in
# between each number.

import random

def generate_int_pairs(filename, n):
    f = open(filename, 'w')
    for _ in range(n):
        p = random.randint(0, 300)
        q = random.randint(0, 300)
        line = str(p) + ' ' + str(q) + '\n'
        f.write(line)
    f.close()

# Sample output:
generate_int_pairs('scores.txt', 6)
# sample contents of 'scores.txt'
# -> 55 251
# -> 83 245
# -> 143 163
# -> 27 158
# -> 244 20



# Exercise 5:
# Your input file will contains results of bowling matches
# between two teams. There will be two scores per line, separated
# by a single space.
#
# Write a function that accepts the name of a file with scores
# and the names of both teams, and prints out an announcement of
# results.
#
# Example: for teams "Red Skins" and "Blue Jays", and scores
#   143 163
#   27 158
#   155 155
#   244 20
# the announcement should be:
#   Blue Jays scored 163 points against Red Skins, winning by 20 points.
#   Blue Jays scored 158 points against Red Skins, winning by 131 points.
#   At 155 points each, Red Skins and Blue Jays tie.
#   Red Skins scored 244 points against Blue Jays, winning by 224 points.
# The last line of the announcement should declare the series
# winner:
#   Blue Jays win the series by 1 game.
# Or:
#   The series is tied between Red Skins and Blue Jays.
#
# Note the number of point(s)/game(s).

def format_number(n, singular, plural):
    if n == 1:
        return '1 ' + singular
    return str(n) + ' ' + plural

def format_points(n):
    return format_number(n, 'point', 'points')

def format_games(n):
    return format_number(n, 'game', 'games')

def announce_results(scores, red_team, blue_team):
    red_team_wins = 0
    blue_team_wins = 0
    ties = 0
    f = open(scores)
    for line in f:
        line = line.strip()
        separator = line.find(' ')
        red_team_score = int(line[:separator])
        blue_team_score = int(line[separator + 1:])
        if red_team_score < blue_team_score:
            difference = blue_team_score - red_team_score
            blue_team_wins += 1
            announcement = blue_team + ' scored ' + format_points(blue_team_score) + ' against ' + red_team
            announcement += ', winning by ' + format_points(difference) + '.'
        elif blue_team_score < red_team_score:
            difference = red_team_score - blue_team_score
            red_team_wins += 1
            announcement = red_team + ' scored ' + format_points(red_team_score) + ' against ' + blue_team
            announcement += ', winning by ' + format_points(difference) + '.'
        else:
            ties += 1
            announcement = 'At ' + format_score(red_team_score) + ' each, ' + red_team + ' and ' + blue_team + ' tie.'
        print(announcement)
    if red_team_wins < blue_team_wins:
        difference = blue_team_wins - red_team_wins
        announcement = blue_team + ' win the series by ' + format_games(difference) + '.'
    elif blue_team_wins < red_team_wins:
        difference = red_team_wins - blue_team_wins
        announcement = red_team + ' win the series by ' + format_games(difference) + '.'
    else:
        announcement = 'The series is tied between ' + red_team + ' and ' + blue_team + '.'
    print(announcement)

# Sample output:
announce_results('scores.txt', 'Red Skins', 'Blue Jays')
# -> Red Skins scored 298 points against Blue Jays, winning by 243 points.
# -> Red Skins scored 262 points against Blue Jays, winning by 15 points.
# -> Red Skins scored 279 points against Blue Jays, winning by 228 points.
# -> Blue Jays scored 221 points against Red Skins, winning by 190 points.
# -> Red Skins scored 251 points against Blue Jays, winning by 158 points.
# -> Red Skins win the series by 3 games.
