"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(lst):
    min_value = lst[0][1]
    min_index = 0
    for i in range(len(lst)):
        if lst[i][1] < min_value:
            min_value = lst[i][1]
            min_index = i
    return lst[min_index][0]

print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create lists in a single line of code.
"""

# Example 1
# Create a list of numbers from 0 to 9

numbers = [i for i in range(10)]
print(numbers)

# Example 2
# Create a list of squares of numbers from 0 to 9

squares = [i**2 for i in range(10)]
print(squares)

# Example 3
# Create a list of even numbers from 0 to 9

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Example 4
# Create a list of odd numbers from 0 to 9

odd_numbers = [i for i in range(10) if i % 2!= 0]
print(odd_numbers)

# Example 5
# Create a list of numbers from 0 to 9 that are divisible by 3

divisible_by_3 = [i for i in range(10) if i % 3 == 0]
print(divisible_by_3)

# Example 6
# Create a list of numbers from 0 to 9 that are divisible by 3 and 5

divisible_by_3_and_5 = [i for i in range(10) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)

# Example 7
# Create a list of numbers from 0 to 9 that are divisible by 3 or 5

divisible_by_3_or_5 = [i for i in range(10) if i % 3 == 0 or i % 5 == 0]
print(divisible_by_3_or_5)

# Example 8
# Create a list of numbers from 0 to 9 that are divisible by 3 and not 5

divisible_by_3_not_5 = [i for i in range(10) if i % 3 == 0 and i % 5!= 0]
print(divisible_by_3_not_5)

# Example 9
# Create a list of numbers from 0 to 9 that are divisible by 3 or not 5

divisible_by_3_or_not_5 = [i for i in range(10) if i % 3 == 0 or i % 5!= 0]
print(divisible_by_3_or_not_5)

# Example 10
# Create a list of numbers from 0 to 9 that are divisible by 3 and 5 or not 5

divisible_by_3_and_5_or_not_5 = [i for i in range(10) if i % 3 == 0 and i % 5 == 0 or i % 5!= 0]
print(divisible_by_3_and_5_or_not_5)

# Example 11
# Create a list of numbers from 0 to 9 that are divisible by 3 and 5 or 5

divisible_by_3_and_5_or_5 = [i for i in range(10)