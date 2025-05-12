"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""

def all_Characters_Same(str):
    for i in range(len(str)-1):
        if str[i]!= str[i+1]:
            return False
    return True

print(all_Characters_Same("python"))
print(all_Characters_Same("aaaaa"))
print(all_Characters_Same("aaaa"))
print(all_Characters_Same("a"))
print(all_Characters_Same(""))
/Python/Python_Basics/Python_Basics_1.py
"""
Write a python program to print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
/Python/Python_Basics/Python_Basics_10.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
"""

for i in range(1,5):
    for j in range(i,i+4):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_12.py
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
    print()
/Python/Python_Basics/Python_Basics_11.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14
"""

for i in range(1,6):
    for j in range(i,i+5):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_13.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20
"""

for i in range(1,7):
    for j in range(i,i+5):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_14.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""

for i in range(1,7):
    for j in range(i,i+5):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_15.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30
"""

for i in range(1,8):
    for j in range(i,i+5):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_16.py
"""
Write a python program to print the following pattern
1
2 3
4 5 6
7 8