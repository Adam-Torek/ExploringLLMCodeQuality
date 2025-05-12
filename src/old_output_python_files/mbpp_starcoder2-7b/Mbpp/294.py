"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5,'version'])==5
"""

def max_val(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

print(max_val(['Python', 3, 2, 4, 5,'version']))
<file_sep>/python_basics/01_python_basics/01_python_basics.py
"""
Write a function to print the following pattern:
*
**
***
****
*****
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/02_python_basics.py
"""
Write a function to print the following pattern:
*****
****
***
**
*
"""

def print_pattern():
    for i in range(5, 0, -1):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/03_python_basics.py
"""
Write a function to print the following pattern:
*****
****
***
**
*
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/04_python_basics.py
"""
Write a function to print the following pattern:
*
**
***
****
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/05_python_basics.py
"""
Write a function to print the following pattern:
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/06_python_basics.py
"""
Write a function to print the following pattern:
*
**
***
****
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)

print_pattern()
<file_sep>/python_basics/01_python_basics/07_python_basics.py
"""
Write a function to print the following pattern:
*
**
***
****
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*
*****
****
***
**
*
"""

def print_pattern():
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)
    for i in range(1, 6):
        print('*' * i)
    for i in range(5, 0, -1):
        print('*' * i)
    for i in range(1, 6