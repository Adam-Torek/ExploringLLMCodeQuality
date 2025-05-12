"""
Write a function to find then'th lucas number.
assert find_lucas(9) == 76
"""

def find_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return find_lucas(n-1) + find_lucas(n-2)

print(find_lucas(9))
<file_sep>/01_python/02_lists/01_list_basics.py
"""
List basics
"""

# Create a list
my_list = [1, 2, 3, 4, 5]

# Access an element
print(my_list[0])

# Change an element
my_list[0] = 10
print(my_list)

# Add an element
my_list.append(6)
print(my_list)

# Remove an element
my_list.pop(0)
print(my_list)

# Remove an element by value
my_list.remove(6)
print(my_list)

# Get the index of an element
print(my_list.index(5))

# Check if an element is in the list
print(5 in my_list)

# Get the length of the list
print(len(my_list))

# Reverse the list
my_list.reverse()
print(my_list)

# Sort the list
my_list.sort()
print(my_list)

# Create a list of lists
my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list_of_lists)

# Access an element of a list of lists
print(my_list_of_lists[0][1])

# Add a list to a list
my_list.extend([10, 11, 12])
print(my_list)

# Create a list of strings
my_list_of_strings = ["a", "b", "c"]
print(my_list_of_strings)

# Create a list of mixed types
my_list_of_mixed_types = [1, "a", True]
print(my_list_of_mixed_types)

# Create a list of lists of strings
my_list_of_lists_of_strings = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(my_list_of_lists_of_strings)

# Create a list of lists of lists
my_list_of_lists_of_lists = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print(my_list_of_lists_of_lists)
<file_sep>/01_python/01_basics/02_variables.py
"""
Variables
"""

# Create a variable
x = 10

# Print a variable
print(x)

# Change the value of a variable
x = 20
print(x)

# Create multiple variables
x = 10
y = 20
z = 30
print(x, y, z)

# Create multiple variables on one line
x, y, z = 10, 20, 30
print(x, y, z)

# Create a variable with a string
name = "John"
print(name)

# Create a variable with a boolean
is_cool = True
print(is_cool)

# Create a variable with a float
price = 10.5
print(price)

# Create a variable with a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Create a variable with a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Create a variable with a set
my_set = {1, 2, 3, 4, 5}
print(my