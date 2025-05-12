"""
Write a function to extract values between quotation marks " " of the given string.
assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53','multi', 'Processor']
"""

def extract_quotation(string):
    return [string[i:j] for i, j in zip(string.find('"') + 1::2, string.find('"')::2)]

print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))
/python/list_comprehension.py
"""
List comprehension is a way to create a list from another list.
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

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 4

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 5

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 6

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 7

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 8

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 9

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 10

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 11

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 12

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 13

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 14

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 15

# Create a list of even numbers from 0 to 9
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)