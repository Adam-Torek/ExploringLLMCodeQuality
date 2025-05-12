"""
Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.
assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])
"""

def larg_nnum(l,n):
    l.sort()
    return l[-n:]

print(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function that takes in a list of numbers and returns the largest number in the list.
assert largest([10,20,50,70,90,20,50,40,60,80,100])==100
"""

def largest(l):
    return max(l)

print(largest([10,20,50,70,90,20,50,40,60,80,100]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function that takes in a list of numbers and returns the smallest number in the list.
assert smallest([10,20,50,70,90,20,50,40,60,80,100])==10
"""

def smallest(l):
    return min(l)

print(smallest([10,20,50,70,90,20,50,40,60,80,100]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function that takes in a list of numbers and returns the second largest number in the list.
assert second_largest([10,20,50,70,90,20,50,40,60,80,100])==90
"""

def second_largest(l):
    l.sort()
    return l[-2]

print(second_largest([10,20,50,70,90,20,50,40,60,80,100]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes in a list of numbers and returns the second smallest number in the list.
assert second_smallest([10,20,50,70,90,20,50,40,60,80,100])==20
"""

def second_smallest(l):
    l.sort()
    return l[1]

print(second_smallest([10,20,50,70,90,20,50,40,60,80,100]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function that takes in a list of numbers and returns the second smallest number in the list.
assert second_smallest([10,20,50,70,90,20,50,40,60,80,100])==20
"""

def second_smallest(l):
    l.sort()
    return l[1]

print(second_smallest([10,20,50,70,90,20,50,40,60,80,100]))