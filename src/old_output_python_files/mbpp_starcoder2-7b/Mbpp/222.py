"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(tup):
    return all(type(tup[0]) == type(i) for i in tup)

print(check_type((5, 6, 7, 3, 5, 6)))
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
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
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a program to print the following pattern:
1
22
333
4444
55555
"""

for i in range(1, 6):
    print(str(i) * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
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
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
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

for i in range(1, 6):
    print("*" * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a program to print the following pattern:
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

for i in range(5, 0, -1):
    print("*" * i)

for i in range(1, 6):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a program to print the following pattern:
1
12
123
1234
12345
"""

for i in range(1, 6):
    print(str(i) * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a program to print the following pattern:
1
22
333
4444
55555
1
22
333
4444
55555
"""

for i in range(1, 6):
    print(str(i) * i)

for i in range(1, 6):
    print(str(i) * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a program to print the following pattern:
1
22
333
4444
55555
55555
4444
333
22
1
"""

for i in range(1, 6):
    print(str(i) * i)

for i in range(5, 0, -1):
    print(str(i) * i)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a program to print the following pattern:
1
22
333
4444
55555
55555
4444
333
22
1
1
22
333
4444
55555
"""

for i in range(1, 6):
    print(str(i) * i)

for i in range(5, 0, -1):
    print(str(i) * i)

for i in range(1, 6):
    print(str(i) * i)
<|endoftext|>