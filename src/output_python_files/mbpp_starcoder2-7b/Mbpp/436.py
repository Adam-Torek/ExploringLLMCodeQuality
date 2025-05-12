"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""

def neg_nos(nums):
    return [num for num in nums if num < 0]

assert neg_nos([-1,4,5,-6]) == [-1,-6]
/python/01_basics/02_lists/01_list_basics.py
"""
List basics
"""

# Create a list
my_list = [1, 2, 3]

# Accessing elements
print(my_list[0])

# Slicing
print(my_list[1:])

# Length
print(len(my_list))

# Append
my_list.append(4)
print(my_list)

# Insert
my_list.insert(1, 10)
print(my_list)

# Remove
my_list.remove(10)
print(my_list)

# Pop
my_list.pop()
print(my_list)

# Reverse
my_list.reverse()
print(my_list)

# Sort
my_list.sort()
print(my_list)

# Copy
my_list_copy = my_list.copy()
print(my_list_copy)

# Clear
my_list.clear()
print(my_list)
/python/01_basics/01_variables/01_variables.py
"""
Variables
"""

# Assigning a value to a variable
a = 1

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning multiple values to multiple variables
a, b, c = 1, 2, 3

# Printing the values of multiple variables
print(a, b, c)

# Printing the type of multiple variables
print(type(a), type(b), type(c))

# Assigning the same value to multiple variables
a = b = c = 1

# Printing the values of multiple variables
print(a, b, c)

# Printing the type of multiple variables
print(type(a), type(b), type(c))

# Assigning a value to a variable using the assignment operator
a = 1

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a += 1

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a -= 1

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a *= 2

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a /= 2

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a %= 2

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a **= 2

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))

# Assigning a value to a variable using the assignment operator
a //= 2

# Printing the value of a variable
print(a)

# Printing the type of a variable
print(type(a))
/python/01_basics/03_dictionaries/01_dictionary_basics.py
"""
Dictionary basics
"""

# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,