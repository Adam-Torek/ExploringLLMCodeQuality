"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_At_One_Bit_Pos(num1,num2):
    return bin(num1^num2).count('1') == 1

print(differ_At_One_Bit_Pos(13,9))
<file_sep>/Python/Python_Basics/Python_Basics_1.py
"""
Write a python program to print the following pattern
*
**
***
****
*****
"""

for i in range(1,6):
    print('*'*i)
<file_sep>/Python/Python_Basics/Python_Basics_10.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
"""

for i in range(1,6):
    print(str(i)*i)
<file_sep>/Python/Python_Basics/Python_Basics_12.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_14.py
"""
Write a python program to print the following pattern
1
23
456
78910
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(i,i+5)))
<file_sep>/Python/Python_Basics/Python_Basics_15.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_13.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_11.py
"""
Write a python program to print the following pattern
1
22
333
4444
55555
"""

for i in range(1,6):
    print(str(i)*i)
<file_sep>/Python/Python_Basics/Python_Basics_16.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_17.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_18.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_19.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str(j) for j in range(1,i+1)))
<file_sep>/Python/Python_Basics/Python_Basics_20.py
"""
Write a python program to print the following pattern
1
12
123
1234
12345
"""

for i in range(1,6):
    print(''.join(str