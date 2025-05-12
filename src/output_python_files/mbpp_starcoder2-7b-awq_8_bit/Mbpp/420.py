"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_Sum(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 == 0:
            sum += i**3
    return sum

print(cube_Sum(2))
/python/list_comprehension.py
"""
List comprehension is an elegant way to create new list from existing list(s).

Write a python function to create a list of cubes of first n natural numbers.
assert cube_List(2) == [1, 8]
"""
def cube_List(n):
    return [i**3 for i in range(1,n+1)]

print(cube_List(2))
/python/list_comprehension_2.py
"""
List comprehension is an elegant way to create new list from existing list(s).

Write a python function to create a list of cubes of first n natural numbers.
assert cube_List(2) == [1, 8]
"""
def cube_List(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List(2))
/python/list_comprehension_3.py
"""
List comprehension is an elegant way to create new list from existing list(s).

Write a python function to create a list of cubes of first n natural numbers.
assert cube_List(2) == [1, 8]
"""
def cube_List(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List(2))

def cube_List_2(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_2(2))
/python/list_comprehension_4.py
"""
List comprehension is an elegant way to create new list from existing list(s).

Write a python function to create a list of cubes of first n natural numbers.
assert cube_List(2) == [1, 8]
"""
def cube_List(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List(2))

def cube_List_2(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_2(2))

def cube_List_3(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_3(2))

def cube_List_4(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_4(2))

def cube_List_5(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_5(2))

def cube_List_6(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_6(2))

def cube_List_7(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_7(2))

def cube_List_8(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_8(2))

def cube_List_9(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_9(2))

def cube_List_10(n):
    return [i**3 for i in range(1,n+1) if i%2 == 0]

print(cube_List_10(2))

def cube_List_11(n