"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""

def freq_count(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
<file_sep>/python/python_basics/python_basics_001.py
"""
Write a function to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

pattern(5)
<file_sep>/python/python_basics/python_basics_002.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_basics/python_basics_003.py
"""
Write a function to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

pattern(5)
<file_sep>/python/python_basics/python_basics_004.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_basics/python_basics_005.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_basics/python_basics_006.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_basics/python_basics_007.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_basics/python_basics_008.py
"""
Write a function to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i,i+n):
            print(j,end=" ")
        print()

pattern(4)
<file_sep>/python/python_