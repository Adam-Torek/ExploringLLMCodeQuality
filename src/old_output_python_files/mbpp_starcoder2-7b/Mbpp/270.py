"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""

def sum_even_and_even_index(lst):
    sum = 0
    for i in range(0, len(lst), 2):
        sum += lst[i]
    return sum

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))
<file_sep>/python/python_basics/01_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
<file_sep>/python/python_basics/04_if_else.py
"""
Write a python program to check whether a number is even or odd.
"""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
<file_sep>/python/python_basics/05_if_elif_else.py
"""
Write a python program to check whether a number is positive, negative or zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
<file_sep>/python/python_basics/03_while_loop.py
"""
Write a python program to print the numbers from 1 to 10.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
<file_sep>/python/python_basics/02_for_loop.py
"""
Write a python program to print the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)
<file_sep>/python/python_basics/06_for_loop_with_range.py
"""
Write a python program to print the numbers from 1 to 10.
"""

for i in range(1, 11):
    print(i)

# range(start, stop, step)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)
<file_sep>/python/python_basics/07_for_loop_with_list.py
"""
Write a python program to print the numbers from 1 to 10.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    print(i)
<file_sep>/python/python_basics/08_for_loop_with_string.py
"""
Write a python program to print the characters of a string.
"""

str = "Hello World"

for i in str:
    print(i)
<file_sep>/python/python_basics/09_for_loop_with_tuple.py
"""
Write a python program to print the characters of a tuple.
"""

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in tup:
    print(i)
<file_sep>/python/python_basics/10_for_loop_with_dictionary.py
"""
Write a python program to print the keys of a dictionary.
"""

dic = {
    "name": "<NAME>",
    "age": 20,
    "gender": "male"
}

for i in dic:
    print(i)
<file_sep>/python/python_basics/11_for_loop_with_set.py
"""
Write a python program to print the elements of a set.
"""

st = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in st:
    print(i)
<file_sep>/python/python_basics/12_for_loop_with_range_and_list.py
"""
Write a python program to print the numbers from 1 to 10.
"""

lst =