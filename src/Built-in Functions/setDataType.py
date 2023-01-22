# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# a set cannot have mutable elements

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create an empty set
empty_set = set()

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)

# how to add new element
numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers)

# how to remove the element

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:', languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)

# how to update sets

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
