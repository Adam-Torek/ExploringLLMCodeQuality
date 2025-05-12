"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""

def replace_specialchar(string):
    return string.replace(' ','::').replace(',','::').replace('.','::')

print(replace_specialchar('Python language, Programming language.'))/python_basics/python_basics_01.py
"""
Write a function to print the following pattern
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""

def print_pattern(n):
    for i in range(1,n+1):
        print(str(i)*i)

print_pattern(9)/python_basics/python_basics_02.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
123456
1234567
12345678
123456789
"""

def print_pattern(n):
    for i in range(1,n+1):
        print(''.join([str(j) for j in range(1,i+1)]))

print_pattern(9)/python_basics/python_basics_03.py
"""
Write a function to print the following pattern
1
11
111
1111
11111
111111
1111111
11111111
111111111
"""

def print_pattern(n):
    for i in range(1,n+1):
        print(''.join([str(i) for j in range(1,i+1)]))

print_pattern(9)/python_basics/python_basics_04.py
"""
Write a function to print the following pattern
1
12
123
1234
12345
123456
1234567
12345678
123456789
12345678910
"""

def print_pattern(n):
    for i in range(1,n+1):
        print(''.join([str(j) for j in range(1,i+1)]))
    for i in range(n-1,0,-1):
        print(''.join([str(j) for j in range(1,i+1)]))

print_pattern(10)/python_basics/python_basics_05.py
"""
Write a function to print the following pattern
1
11
111
1111
11111
111111
1111111
11111111
111111111
1111111111
11111111111
111111111111
1111111111111
11111111111111
111111111111111
1111111111111111
11111111111111111
111111111111111111
1111111111111111111
"""

def print_pattern(n):
    for i in range(1,n+1):
        print(''.join([str(j) for j in range(1,i+1)]))
    for i in range(n-1,0,-1):
        print(''.join([str(j) for j in range(1,i+1)]))

print_pattern(20)/python_basics/python_basics_06.py
"""
Write a function to print the following pattern
1