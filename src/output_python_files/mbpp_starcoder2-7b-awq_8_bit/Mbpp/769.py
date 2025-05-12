"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(list1, list2):
    return [x for x in list1 if x not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_1.py
"""
Write a python function to get the sum of two lists.
assert (Sum([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == 130
"""

def Sum(list1, list2):
    return sum(list1) + sum(list2)

print(Sum([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_3.py
"""
Write a python function to get the largest number in a list.
assert (Max([10, 15, 20, 25, 30, 35, 40])) == 40
"""

def Max(list1):
    return max(list1)

print(Max([10, 15, 20, 25, 30, 35, 40]))
/Python/Python_Basics/Python_Basics_2.py
"""
Write a python function to get the smallest number in a list.
assert (Min([10, 15, 20, 25, 30, 35, 40])) == 10
"""

def Min(list1):
    return min(list1)

print(Min([10, 15, 20, 25, 30, 35, 40]))