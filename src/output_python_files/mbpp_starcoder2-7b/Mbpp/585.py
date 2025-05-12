"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(items, n):
    return sorted(items, key=lambda x: x['price'], reverse=True)[:n]

print(expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1))
/python/python_basics/03_lists/03_list_comprehension.py
"""
List comprehension is a way to create a list in a single line of code.
"""

# Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# Create a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Create a list of numbers from 1 to 100 that are divisible by 3
divisible_by_3 = [x for x in range(1, 101) if x % 3 == 0]
print(divisible_by_3)

# Create a list of numbers from 1 to 100 that are divisible by 3 and 5
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)

# Create a list of numbers from 1 to 100 that are divisible by 3 or 5
divisible_by_3_or_5 = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
print(divisible_by_3_or_5)

# Create a list of numbers from 1 to 100 that are divisible by 3 and not 5
divisible_by_3_not_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5!= 0]
print(divisible_by_3_not_5)

# Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both
divisible_by_3_or_5_not_both = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 and x % 15!= 0]
print(divisible_by_3_or_5_not_both)

# Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both
divisible_by_3_or_5_not_both = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 and x % 15!= 0]
print(divisible_by_3_or_5_not_both)

# Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both
divisible_by_3_or_5_not_both = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 and x % 15!= 0]
print(divisible_by_3_or_5_not_both)

# Create a list of numbers from 1 to 100 that are divisible by 3 or 5 but not both
divisible_by_3_or_5_not_both = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0 and x % 15!= 0]
print(divisible_by_3_or_5_not