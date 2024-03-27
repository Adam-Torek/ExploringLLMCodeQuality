"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(li1, li2):
    return [x for x in li1 if x not in li2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python program to print the following pattern
1
11
111
1111
11111
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python program to print the following pattern
1
23
456
78910
"""

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
666666
"""

for i in range(1, 7):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
666666
7777777
"""

for i in range(1, 8):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
666666
7777777
88888888
"""

for i in range(1, 9):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a python program to print the following pattern
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

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, end="")
    print()
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
666666