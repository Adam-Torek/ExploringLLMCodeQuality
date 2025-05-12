"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(lst,n):
    xor_sum = 0
    for i in range(n):
        xor_sum = xor_sum ^ lst[i]
    return xor_sum

print(pair_xor_Sum([5,9,7,6],4))
/Python/Python_Basics/Python_Basics_1.py
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
    print()
/Python/Python_Basics/Python_Basics_10.py
"""
Write a python program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_11.py
"""
Write a python program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Another way

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
/Python/Python_Basics/Python_Basics_12.py
"""
Write a python program to print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Another way

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Another way

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Another way

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Another way

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()