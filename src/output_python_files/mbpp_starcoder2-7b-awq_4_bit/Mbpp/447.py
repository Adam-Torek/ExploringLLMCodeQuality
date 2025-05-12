"""
Write a function to find cubes of individual elements in a list.
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

def cube_nums(nums):
    return [num**3 for num in nums]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
/python_basics/list_comprehension.py
"""
List comprehension is a way to create lists in a concise way.
"""

# Example 1

# Without list comprehension

nums = []
for num in range(10):
    nums.append(num)

print(nums)

# With list comprehension

nums = [num for num in range(10)]

print(nums)

# Example 2

# Without list comprehension

nums = []
for num in range(10):
    if num % 2 == 0:
        nums.append(num)

print(nums)

# With list comprehension

nums = [num for num in range(10) if num % 2 == 0]

print(nums)

# Example 3

# Without list comprehension

nums = []
for num in range(10):
    if num % 2 == 0:
        nums.append(num**2)

print(nums)

# With list comprehension

nums = [num**2 for num in range(10) if num % 2 == 0]

print(nums)

# Example 4

# Without list comprehension

nums = []
for num in range(10):
    if num % 2 == 0:
        nums.append(num**2)
    else:
        nums.append(num**3)

print(nums)

# With list comprehension

nums = [num**2 if num % 2 == 0 else num**3 for num in range(10)]

print(nums)
/python_basics/functions.py
"""
Functions are a way to group a set of statements together.
"""

# Example 1

def say_hello():
    print("Hello")

say_hello()

# Example 2

def say_hello(name):
    print("Hello " + name)

say_hello("John")

# Example 3

def say_hello(name="John"):
    print("Hello " + name)

say_hello()

# Example 4

def say_hello(name="John"):
    print("Hello " + name)

say_hello("Jane")

# Example 5

def say_hello(name="John"):
    return "Hello " + name

print(say_hello())

# Example 6

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane"))

# Example 7

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 8

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 9

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 10

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 11

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 12

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("Jane") + "!")

# Example 13

def say_hello(name="John"):
    return "Hello " + name

print(say_hello("J