"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_Swaps(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i]!= s2[i]:
            count += 1
    return count

print(min_Swaps("1101","1110"))<file_sep>/Python/Python_Basics/Python_Basics_1.py
"""
Write a python program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_10.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

for i in range(1,5):
    for j in range(i,i+3):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_12.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_11.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9
"""

for i in range(1,5):
    for j in range(i,i+4):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_13.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9
10 11 12 13
"""

for i in range(1,5):
    for j in range(i,i+4):
        print(j,end=" ")
    print()

for i in range(5,10):
    for j in range(i,i+4):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_14.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9
10 11 12 13
14 15 16 17 18
"""

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end=" ")
    print()

for i in range(6,11):
    for j in range(i,i+5):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_15.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9
10 11 12 13
14 15 16 17 18
19 20 21 22 23 24
"""

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end=" ")
    print()

for i in range(6,11):
    for j in range(i,i+5):
        print(j,end=" ")
    print()

for i in range(11,16):
    for j in range(i,i+6):
        print(j,end=" ")
    print()<file_sep>/Python/Python_Basics/Python_Basics_16.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9
10 11 12 13
14 15 16 17 18
1