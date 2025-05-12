"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""

def split(string):
    return [char for char in string]

print(split('python'))
/python/python_basics/02_variables.py
"""
Write a python program to print the following string in a specific format (see the output).
"""

name = "John"
age = 23

print("My name is %s and I am %d years old." % (name, age))
/python/python_basics/03_operators.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
/python/python_basics/01_hello_world.py
"""
Write a python program to print the following string in a specific format (see the output).
"""

print("Hello World!")
/python/python_basics/04_if_else.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
/python/python_basics/05_for_loop.py
"""
Write a python program to print the result of the following operations.
"""

for i in range(1, 11):
    print(i)
/python/python_basics/06_while_loop.py
"""
Write a python program to print the result of the following operations.
"""

i = 1
while i <= 10:
    print(i)
    i += 1
/python/python_basics/07_functions.py
"""
Write a python function to add two numbers.
assert add(10, 20) == 30
"""

def add(a, b):
    return a + b

print(add(10, 20))
/python/python_basics/08_lists.py
"""
Write a python program to print the result of the following operations.
"""

a = [1, 2, 3, 4, 5]

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

print(a[0:3])
print(a[1:4])
print(a[2:5])
print(a[3:6])
print(a[4:7])

print(a[0:5:2])
print(a[1:5:2])
print(a[2:5:2])
print(a[3:6:2])
print(a[4:7:2])

print(a[::-1])
print(a[::-2])

a.append(6)
print(a)

a.insert(0, 0)
print(a)

a.remove(0)
print(a)

a.pop()
print(a)

a.pop(0)
print(a)

a.clear()
print(a)
/python/python_basics/09_dictionaries.py
"""
Write a python program to print the result of the following operations.
"""

a = {
    'name': 'John',
    'age': 23,
    'city': 'New York'
}

print(a['name'])
print(a['age'])
print(a['city'])

a['name'] = 'Jane'
print(a)

a['country'] = 'USA'
print(a)

del a['country']
print(a)

a.clear()
print