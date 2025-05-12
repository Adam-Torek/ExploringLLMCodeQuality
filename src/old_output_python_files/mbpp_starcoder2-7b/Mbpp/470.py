"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""

def add_pairwise(tup):
    return tuple(tup[i] + tup[i+1] for i in range(len(tup)-1))

print(add_pairwise((1, 5, 7, 8, 10)))
<file_sep>/python_basics/002_variables.py
"""
Write a program to print the following pattern:
*
**
***
****
*****
"""

for i in range(1, 6):
    print("*" * i)

"""
Write a program to print the following pattern:
*****
****
***
**
*
"""

for i in range(5, 0, -1):
    print("*" * i)

"""
Write a program to print the following pattern:
1
12
123
1234
12345
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1)))

"""
Write a program to print the following pattern:
1
23
456
78910
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(i, i+5)))

"""
Write a program to print the following pattern:
1
22
333
4444
55555
"""

for i in range(1, 6):
    print("".join(str(i) * i))

"""
Write a program to print the following pattern:
1
22
333
4444
55555
666666
"""

for i in range(1, 7):
    print("".join(str(i) * i))

"""
Write a program to print the following pattern:
1
12
123
1234
12345
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1)))

"""
Write a program to print the following pattern:
1
23
456
78910
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(i, i+5)))

"""
Write a program to print the following pattern:
1
22
333
4444
55555
666666
"""

for i in range(1, 7):
    print("".join(str(i) * i))

"""
Write a program to print the following pattern:
1
23
456
78910
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1)))

"""
Write a program to print the following pattern:
1
22
333
4444
55555
666666
"""

for i in range(1, 7):
    print("".join(str(i) * i))

"""
Write a program to print the following pattern:
1
23
456
78910
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1)))

"""
Write a program to print the following pattern:
1
22
333
4444
55555
666666
"""

for i in range(1, 7):
    print("".join(str(i) * i))

"""
Write a program to print the following pattern:
1
23
456
78910
"""

for i in range(1, 6):
    print("".join(str(j) for j in range(1, i+1)))

"""
Write a program to print the following pattern:
1
22