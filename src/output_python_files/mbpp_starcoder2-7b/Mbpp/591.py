"""
Write a python function to interchange the first and last elements in a list.
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""

def swap_List(list):
    list[0], list[-1] = list[-1], list[0]
    return list

print(swap_List([12, 35, 9, 56, 24]))
<file_sep>/python_basics/01_python_basics/02_variables.py
"""
Write a python program to print the following string in a specific format (see the output).
"""

name = "<NAME>"
age = 23

print("My name is %s and I am %d years old." % (name, age))
<file_sep>/python_basics/01_python_basics/03_operators.py
"""
Write a python program to print the result of the following operations.
"""

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
<file_sep>/python_basics/01_python_basics/04_conditional_statements.py
"""
Write a python program to print the result of the following conditional statements.
"""

a = 10
b = 5

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
<file_sep>/python_basics/01_python_basics/05_loops.py
"""
Write a python program to print the result of the following loops.
"""

for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1
<file_sep>/python_basics/01_python_basics/06_functions.py
"""
Write a python function to find the maximum of three numbers.
assert max_of_three(10, 11, 9) == 11
"""

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_of_three(10, 11, 9))
<file_sep>/python_basics/01_python_basics/07_lists.py
"""
Write a python program to print the result of the following lists.
"""

list = [1, 2, 3, 4, 5]

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])

print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])

print(list[0:3])
print(list[1:4])
print(list[2:5])
print(list[3:6])
print(list[4:7])

print(list[0:5:2])
print(list[1:5:2])
print(list[2:5:2])
print(list[3:6:2])
print(list[4:7:2])

print(list[::-1])
print(list[::-2])

list.append(6)
print(list)

list.insert(0, 0)
print(list)

list.remove(6)
print(list)

list.pop()
print(list)

list.pop(0)
print(list)

list.clear()
print(list)
<file_sep>/python_basics/01_python_basics/08_dictionaries.py
"""
Write a python program to print the result of the following dictionaries.
"""

dict = {
    "name": "<NAME>",
    "age": 23,
    "city": "Sofia"
}

print(dict["name"])
print(dict["age"])
print(dict["city"])

print(dict.