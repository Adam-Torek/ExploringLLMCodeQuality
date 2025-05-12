"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n,words):
    return [word for word in words if len(word)>n]

print(long_words(3,"python is a programming language"))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1
# Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)

# Example 2
# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 3
# Create a list of squares of numbers from 0 to 9
squares = [i ** 2 for i in range(10)]
print(squares)

# Example 4
# Create a list of cubes of numbers from 0 to 9
cubes = [i ** 3 for i in range(10)]
print(cubes)

# Example 5
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10)]
print(tuples)

# Example 6
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 7
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 8
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 9
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 10
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 11
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 12
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 13
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 14
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 15
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if i % 2 == 0]
print(tuples)

# Example 16
# Create a list of tuples of numbers from 0 to 9
tuples = [(i, i ** 2, i ** 3) for i in range(10) if