# Processing Lists
# ----------------
# Two of the most common operations on a list are modifying
# each element of a list, and excluding elements of a list.
#
# A function that accepts an element of a list and returns
# a modified value for that element is called a map function.
#
# A function that accepts an element of a list and returns
# whether the element should be kept or excluded is called
# a filter function.
#
# For example, given a list of numbers, we want to produce
# another list which contains the squares of only the even
# numbers in the list.

def even_squares(t):
    result = []
    for e in t:
        if e % 2 == 0:
            result.append(e ** 2)
    return result

naturals = [1, 2, 3, 4, 5]
es = even_squares(naturals)
print('naturals ==', naturals)
print('es ==', es)

# A nested list is a list within a list.
# Using the above idiom, we can create lists of lists as well.

# For example, let's produce a list whose elements are lists
# containing the number and its square.

def number_square_pairs(t):
    result = []
    for e in t:
        result.append([e, e ** 2])
    return result

nsp = number_square_pairs(naturals)
print('naturals ==', naturals)
print('nsp ==', nsp)

names = ['alaa', 'fiha', 'amna', 'hamza', 'mahnoor', 'hajra', 'safina', 'dua']

def map_to_upper(t):
    result = []
    for e in t:
        result.append(e.upper())
    return result

upper_names = map_to_upper(names)
print('names ==', names)
print('upper_names ==', upper_names)

# In general, a function that both maps and filters a list has
# the following pattern:

def map_filter_list(t):
    result = []
    for e in t:
        if filter_func(e):
            result.append(map_true_func(e))
        else:
            result.append(map_false_func(e))
    return result

# where:
# map_*_func takes one element as its argument and returns
# its modified value; and
# filter_func takes one element as its argument and returns
# True if the element is kept, False if it is to be excluded.



# Exercise 1a
# Write a function which accepts a list of numbers and an
# exponent as arguments and returns a list of numbers with each
# element raised to the exponent.

def exponents(t, exp):
    result = []
    for e in t:
        result.append(e ** exp)
    return result

print('naturals ==', naturals)
print('exponents(naturals, 2) ==', exponents(naturals, 2))
# -> [1, 4, 9, 16, 25]

# Exercise 1b
# Modify the above function such that it produces nested lists
# which contain the number and its exponent.

def number_exponent_pairs(t, exp):
    result = []
    for e in t:
        result.append([e, e ** exp])
    return result

print('number_exponent_pairs(naturals, 2) ==', number_exponent_pairs(naturals, 2))
# -> [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]

# Exercise 1c
# Modify the above function such that it only return the odd
# numbers in a given list and their exponent.

def odd_number_exponent_pairs(t, exp):
    result = []
    for e in t:
        if e % 2 == 1:
            result.append([e, e ** exp])
    return result

print('odd_number_exponent_pairs(naturals, 2) ==', odd_number_exponent_pairs(naturals, 2))
# -> [[1, 1], [3, 9], [5, 25]]



# Exercise 2
# Write a function that returns the list of numbers that are
# divisible by both x and y.

def multiples(t, x, y):
    result = []
    for e in t:
        if e % x == 0 and e % y == 0:
            result.append(e)
    return result

print('multiples(range(50), 2, 5) ==', multiples(range(50), 2, 5))
# -> [0, 10, 20, 30, 40]

# Note: the above pattern works with any sequence (e.g., range).



# Exercise 3
# Write a function that returns a nested list with each element
# and its parity.

def number_parity_pairs(t):
    result = []
    for e in t:
        if e % 2 == 0:
            result.append([e, 'even'])
        else:
            result.append([e, 'odd'])
    return result

print('number_parity_pairs(naturals) ==', number_parity_pairs(naturals))
# -> [[1, 'odd'], [2, 'even'], [3, 'odd'], [4, 'even'], [5, 'odd']]



# Exercise 4a
# Write a function that converts a list of masses in kilograms to
# grams. Note: to convert from kg to g, multiply by one thousand.

def convert_kg_to_g(t):
    result = []
    for e in t:
        result.append(e * 1000)
    return result

print('convert_kg_to_g(naturals) ==', convert_kg_to_g(naturals))
# -> [1000, 2000, 3000, 4000, 5000]

# Exercise 4b
# Write a function that converts a list of masses in kilograms to
# pounds. Note: to convert from kg to lbs, multiply by 2.2046.

def convert_kg_to_lbs(t):
    result = []
    for e in t:
        result.append(e * 2.2046)
    return result

print('convert_kg_to_lbs(naturals) ==', convert_kg_to_lbs(naturals))
# -> [2.2046, 4.4092, 6.6138, 8.8184, 11.023]

# Exercise 4c
# Modify the above funtion to accept the conversion unit as an
# argument and make the appropriate conversion.
# If the unit is unrecognized, return an unmodified list.

def convert_kg_to(t, unit):
    result = []
    for e in t:
        if unit == 'g':
            result.append(e * 1000)
        elif unit == 'lbs':
            result.append(e * 2.2046)
        else:
            result.append(e)
    return result

print("convert_kg_to(naturals, 'g') ==", convert_kg_to(naturals, 'g'))
# -> [1000, 2000, 3000, 4000, 5000]
print("convert_kg_to(naturals, 'lbs') ==", convert_kg_to(naturals, 'lbs'))
# -> [2.2046, 4.4092, 6.6138, 8.8184, 11.023]
print("convert_kg_to(naturals, 'st') ==", convert_kg_to(naturals, 'st'))
# -> [1, 2, 3, 4, 5]

# Alternative:
def convert_kg_to(t, unit):
    if unit == 'g':
        return convert_kg_to_g(t)
    if unit == 'lbs':
        return convert_kg_to_lbs(t)
    # There is a potential bug if the list isn't copied.
    return t.copy()

print("convert_kg_to(naturals, 'g') ==", convert_kg_to(naturals, 'g'))
# -> [1000, 2000, 3000, 4000, 5000]
print("convert_kg_to(naturals, 'lbs') ==", convert_kg_to(naturals, 'lbs'))
# -> [2.2046, 4.4092, 6.6138, 8.8184, 11.023]
print("convert_kg_to(naturals, 'st') ==", convert_kg_to(naturals, 'st'))
# -> [1, 2, 3, 4, 5]



# Exercise 5
# Read a file containing full names and form a nested list where
# every element is a list containing first name and last name.

def first_last_name_pairs(filename):
    f = open(filename)
    names = f.readlines()
    result = []
    for name in names:
        result.append(name.split())
    return result

print("first_last_name_pairs('mynames.txt') ==", first_last_name_pairs('mynames.txt'))
# -> [['Fiha', 'Ali'], ['Hamza', 'Jafri'], ['Mahnoor',
# ->   'Mahboob'], ['Vaneeza', 'Iqbal'], ['Afifa', 'Bashir'],
# ->  ['Aala', 'Siddiqi'], ['Zunairah', 'Qureshi'],
# ->  ['Safina', 'Shalwani']]
