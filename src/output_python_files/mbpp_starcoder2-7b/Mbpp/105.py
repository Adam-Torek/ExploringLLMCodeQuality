"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""

def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

print(count([True,False,True]))
/python/python_basics/01_variables/02_variables.py
"""
Write a python program to print the sum of two numbers.
"""

a = 10
b = 20

print(a + b)
/python/python_basics/03_conditionals/01_conditionals.py
"""
Write a python program to check if the given number is even or odd.
"""

num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
/python/python_basics/02_loops/01_loops.py
"""
Write a python program to print the numbers from 1 to 10.
"""

for i in range(1,11):
    print(i)
/python/python_basics/04_functions/01_functions.py
"""
Write a python function to print the sum of two numbers.
"""

def sum(a,b):
    return a + b

print(sum(10,20))
/python/python_basics/05_lists/01_lists.py
"""
Write a python program to print the sum of all the numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    sum += i

print(sum)
/python/python_basics/05_lists/02_lists.py
"""
Write a python program to print the sum of all the even numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    if i % 2 == 0:
        sum += i

print(sum)
/python/python_basics/05_lists/03_lists.py
"""
Write a python program to print the sum of all the odd numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    if i % 2!= 0:
        sum += i

print(sum)
/python/python_basics/05_lists/04_lists.py
"""
Write a python program to print the sum of all the even numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    if i % 2 == 0:
        sum += i

print(sum)

# using list comprehension

lst = [10,20,30,40]

sum = sum([i for i in lst if i % 2 == 0])

print(sum)
/python/python_basics/05_lists/05_lists.py
"""
Write a python program to print the sum of all the odd numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    if i % 2!= 0:
        sum += i

print(sum)

# using list comprehension

lst = [10,20,30,40]

sum = sum([i for i in lst if i % 2!= 0])

print(sum)
/python/python_basics/05_lists/06_lists.py
"""
Write a python program to print the sum of all the even numbers in the given list.
"""

lst = [10,20,30,40]

sum = 0
for i in lst:
    if i % 2 == 0:
        sum += i

print(sum)

# using list comprehension

lst = [10,2