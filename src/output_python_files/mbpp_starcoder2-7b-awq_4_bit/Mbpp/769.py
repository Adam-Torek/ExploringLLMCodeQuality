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
assert (Sum([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == 150
"""

def Sum(list1, list2):
    return sum(list1) + sum(list2)

print(Sum([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_2.py
"""
Write a python function to get the difference between two lists.
assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
"""

def Diff(list1, list2):
    return [x for x in list1 if x not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_3.py
"""
Write a python function to get the intersection of two lists.
assert (Intersection([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [25, 40, 35]
"""

def Intersection(list1, list2):
    return [x for x in list1 if x in list2]

print(Intersection([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_4.py
"""
Write a python function to get the union of two lists.
assert (Union([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 15, 20, 25, 30, 35, 40, 45]
"""

def Union(list1, list2):
    return list1 + [x for x in list2 if x not in list1]

print(Union([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
/Python/Python_Basics/Python_Basics_5.py
"""
Write a python function to get the symmetric difference of two lists.
assert (SymDiff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 15, 20, 30, 35, 40]
"""

def SymDiff(list1, list2):
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]

print(SymDiff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))