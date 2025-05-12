"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2))
/python/python_basics/02_variables/01_variables.py
"""
Write a python program that prints the following:

My name is 
I am 25 years old
I am 6'2" tall
"""

name = ""
age = 25
height = 6.2

print("My name is " + name)
print("I am " + str(age) + " years old")
print("I am " + str(height) + " tall")
/python/python_basics/03_conditionals/02_conditionals.py
"""
Write a python program that takes in a number and prints out whether it is positive, negative, or zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
/python/python_basics/04_loops/01_loops.py
"""
Write a python program that prints out the numbers 1 to 100.
"""

for i in range(1, 101):
    print(i)
/python/python_basics/03_conditionals/01_conditionals.py
"""
Write a python program that takes in a number and prints out whether it is odd or even.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
/python/python_basics/05_functions/01_functions.py
"""
Write a python function that takes in a number and returns the square of that number.
assert square(2) == 4
"""

def square(num):
    return num**2

print(square(2))
/python/python_basics/06_lists/01_lists.py
"""
Write a python program that takes in a list of numbers and prints out the sum of the numbers.
assert sum_List([1, 2, 3]) == 6
"""

def sum_List(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum_List([1, 2, 3]))
/python/python_basics/06_lists/02_lists.py
"""
Write a python program that takes in a list of numbers and returns the average of the numbers.
assert average_List([1, 2, 3]) == 2
"""

def average_List(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)

print(average_List([1, 2, 3]))
/python/python_basics/06_lists/03_lists.py
"""
Write a python program that takes in a list of numbers and returns the largest number in the list.
assert largest_List([1, 2, 3]) == 3
"""

def largest_List(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

print(largest_List([1, 2, 3]))
/python/python_basics/05_functions/02_functions.py
"""
Write a python function that takes in a number and returns the square root of that number.
assert square_Root(4) == 2
"""

def square_Root(num):
    return num**0.5

print(square_Root(4))
/python/python_basics/06_lists/04_lists.py
"""
Write a python program that takes in a list of numbers and returns the smallest number in the list.
assert smallest_List([1, 2, 3]) == 1
"""

def smallest_List(nums):
    smallest = nums[0]
    for num in nums