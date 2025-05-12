"""
Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).
assert sequential_search([11,23,58,31,56,77,43,12,65,19],31) == (True, 3)
"""

def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)

print(sequential_search([11,23,58,31,56,77,43,12,65,19],31))
<file_sep>/01_python/01_basics/03_lists/03_list_comprehension.py
"""
List comprehension is a way to create a list based on an existing list.

The syntax is:

[expression for item in list]

The expression can be any Python expression, including another list comprehension.

"""

# Example 1

# Create a list of the first letters of each word in the string

words = "The quick brown fox jumps over the lazy dog".split()

# Solution 1

first_letters = []
for word in words:
    first_letters.append(word[0])

print(first_letters)

# Solution 2

first_letters = [word[0] for word in words]

print(first_letters)

# Example 2

# Create a list of the first letters of each word in the string, but only if the word is more than 4 characters long

# Solution 1

first_letters = []
for word in words:
    if len(word) > 4:
        first_letters.append(word[0])

print(first_letters)

# Solution 2

first_letters = [word[0] for word in words if len(word) > 4]

print(first_letters)

# Example 3

# Create a list of the first letters of each word in the string, but only if the word is more than 4 characters long, and the first letter is an "o"

# Solution 1

first_letters = []
for word in words:
    if len(word) > 4 and word[0] == "o":
        first_letters.append(word[0])

print(first_letters)

# Solution 2

first_letters = [word[0] for word in words if len(word) > 4 and word[0] == "o"]

print(first_letters)

# Example 4

# Create a list of the first letters of each word in the string, but only if the word is more than 4 characters long, and the first letter is an "o", and the last letter is an "g"

# Solution 1

first_letters = []
for word in words:
    if len(word) > 4 and word[0] == "o" and word[-1] == "g":
        first_letters.append(word[0])

print(first_letters)

# Solution 2

first_letters = [word[0] for word in words if len(word) > 4 and word[0] == "o" and word[-1] == "g"]

print(first_letters)

# Example 5

# Create a list of the first letters of each word in the string, but only if the word is more than 4 characters long, and the first letter is an "o", and the last letter is an "g", and the word is in all caps

# Solution 1

first_letters = []
for word in words:
    if len(word) > 4 and word[0] == "o" and word[-1] == "g" and word.isupper():
        first_letters.append(word[0])

print(first_letters)

# Solution 2

first_letters = [word[0] for word in words if len(word) > 4 and word[0] == "o" and word[-1] == "g" and word.isupper()]

print(first_letters)

# Example 6

# Create a list of the first letters of each word in