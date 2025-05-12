"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(tuple1, tuple2):
    if len(tuple1)!= len(tuple2):
        return False
    for i in range(len(tuple1)):
        if tuple1[i] >= tuple2[i]:
            return False
    return True

print(check_smaller((1, 2, 3), (2, 3, 4)))
<file_sep>/week01/day04/02_print_bigger.py
"""
Write a function that prints the bigger of two numbers
"""

def print_bigger(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("They are equal")

print_bigger(10, 20)
<file_sep>/week01/day04/03_print_bigger_two.py
"""
Write a function that prints the bigger of two numbers
"""

def print_bigger_two(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("They are equal")

print_bigger_two(10, 20)
<file_sep>/week01/day04/04_print_bigger_three.py
"""
Write a function that prints the biggest of three numbers
"""

def print_bigger_three(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
    else:
        print("They are equal")

print_bigger_three(10, 20, 30)
<file_sep>/week01/day04/01_print_bigger.py
"""
Write a function that prints the bigger of two numbers
"""

def print_bigger(a, b):
    if a > b:
        print(a)
    else:
        print(b)

print_bigger(10, 20)
<file_sep>/week01/day04/05_print_bigger_four.py
"""
Write a function that prints the biggest of four numbers
"""

def print_bigger_four(a, b, c, d):
    if a > b and a > c and a > d:
        print(a)
    elif b > a and b > c and b > d:
        print(b)
    elif c > a and c > b and c > d:
        print(c)
    elif d > a and d > b and d > c:
        print(d)
    else:
        print("They are equal")

print_bigger_four(10, 20, 30, 40)
<file_sep>/week01/day04/06_print_bigger_five.py
"""
Write a function that prints the biggest of five numbers
"""

def print_bigger_five(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        print(a)
    elif b > a and b > c and b > d and b > e:
        print(b)
    elif c > a and c > b and c > d and c > e:
        print(c)
    elif d > a and d > b and d > c and d > e:
        print(d)
    elif e > a and e > b and e > c and e > d:
        print(e)
    else:
        print("They are equal")

print_bigger_five(10, 20, 30, 40, 50)
<file_sep>/week01/day04/07_print_bigger_six.py
"""
Write a function that prints the biggest of six numbers
"""

def print_bigger_six(a, b, c, d, e, f):
    if a > b and a > c and a > d and a > e and a > f:
        print(a)
    elif b > a and b > c and b > d and b > e and b > f:
        print(b)