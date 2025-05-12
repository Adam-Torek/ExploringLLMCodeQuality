"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(list1,list2):
    return [list1[i]-list2[i] for i in range(len(list1))]

print(sub_list([1,2,3],[4,5,6]))
/python/list/list_comprehension.py
"""
List comprehension is a way to create a list based on existing lists.
"""

# Example 1

# Create a list of squares of numbers from 0 to 9

squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

# Using list comprehension

squares = [i**2 for i in range(10)]
print(squares)

# Example 2

# Create a list of cubes of numbers from 0 to 9

cubes = []
for i in range(10):
    cubes.append(i**3)

print(cubes)

# Using list comprehension

cubes = [i**3 for i in range(10)]
print(cubes)

# Example 3

# Create a list of even numbers from 0 to 9

even_numbers = []
for i in range(10):
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

# Using list comprehension

even_numbers = [i for i in range(10) if i%2==0]
print(even_numbers)

# Example 4

# Create a list of odd numbers from 0 to 9

odd_numbers = []
for i in range(10):
    if i%2!=0:
        odd_numbers.append(i)

print(odd_numbers)

# Using list comprehension

odd_numbers = [i for i in range(10) if i%2!=0]
print(odd_numbers)

# Example 5

# Create a list of numbers from 0 to 9 which are divisible by 3

divisible_by_3 = []
for i in range(10):
    if i%3==0:
        divisible_by_3.append(i)

print(divisible_by_3)

# Using list comprehension

divisible_by_3 = [i for i in range(10) if i%3==0]
print(divisible_by_3)

# Example 6

# Create a list of numbers from 0 to 9 which are not divisible by 3

not_divisible_by_3 = []
for i in range(10):
    if i%3!=0:
        not_divisible_by_3.append(i)

print(not_divisible_by_3)

# Using list comprehension

not_divisible_by_3 = [i for i in range(10) if i%3!=0]
print(not_divisible_by_3)

# Example 7

# Create a list of numbers from 0 to 9 which are divisible by 3 and even

divisible_by_3_and_even = []
for i in range(10):
    if i%3==0 and i%2==0:
        divisible_by_3_and_even.append(i)

print(divisible_by_3_and_even)

# Using list comprehension

divisible_by_3_and_even = [i for i in range(10) if i%3==0 and i%2==0]
print(divisible_by_3_and_even)

# Example 8

# Create a list of numbers from 0 to 9 which are divisible by 3 and odd

divisible_by_3_and_odd = []
for i in range(10):
    if i%3==0 and i%2!=0:
        divisible_by_3