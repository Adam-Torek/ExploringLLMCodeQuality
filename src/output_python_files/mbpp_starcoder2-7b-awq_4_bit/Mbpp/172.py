"""
Write a function to count the number of occurence of the string'std' in a given string.
assert count_occurance("letstdlenstdporstd") == 3
"""

def count_occurance(string):
    count = 0
    for i in range(len(string)):
        if string[i:i+3] == "std":
            count += 1
    return count

print(count_occurance("letstdlenstdporstd"))
/python/python_basics/python_basics_1.py
"""
Write a function to print the following pattern
*
**
***
****
*****
"""

def print_pattern(n):
    for i in range(n):
        print("*"*(i+1))

print_pattern(5)
/python/python_basics/python_basics_10.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_11.py
"""
Write a function to print the following pattern
1
22
333
4444
55555
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(i+1)]*(i+1)))

print_pattern(5)
/python/python_basics/python_basics_12.py
"""
Write a function to print the following pattern
1
23
456
78910
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(i*2+1,i*2+7)]))

print_pattern(5)
/python/python_basics/python_basics_13.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_14.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_15.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_16.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_17.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
"""

def print_pattern(n):
    for i in range(n):
        print("".join([str(j) for j in range(1,i+2)]))

print_pattern(5)
/python/python_basics/python_basics_18.py
"""
Write a function to print the following pattern
1
1