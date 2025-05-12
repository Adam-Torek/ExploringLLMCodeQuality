"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""

def Find_Min(l):
    min_len = len(l[0])
    min_list = l[0]
    for i in l:
        if len(i) < min_len:
            min_len = len(i)
            min_list = i
    return min_list

print(Find_Min([[1],[1,2],[1,2,3]]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a python function to find the sum of all the elements in a list.
assert Sum([1,2,3]) == 6
"""

def Sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum

print(Sum([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a python function to find the maximum element in a list.
assert Max([1,2,3]) == 3
"""

def Max(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

print(Max([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a python function to find the average of all the elements in a list.
assert Avg([1,2,3]) == 2
"""

def Avg(l):
    sum = 0
    for i in l:
        sum += i
    return sum/len(l)

print(Avg([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a python function to find the minimum element in a list.
assert Min([1,2,3]) == 1
"""

def Min(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

print(Min([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a python function to find the length of a list.
assert Length([1,2,3]) == 3
"""

def Length(l):
    return len(l)

print(Length([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a python function to find the largest element in a list.
assert Max([1,2,3]) == 3
"""

def Max(l):
    max = l[0]
    for i in l:
        if i > max:
            max = i
    return max

print(Max([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a python function to find the second largest element in a list.
assert Second_Max([1,2,3]) == 2
"""

def Second_Max(l):
    max = l[0]
    second_max = l[0]
    for i in l:
        if i > max:
            second_max = max
            max = i
        elif i > second_max:
            second_max = i
    return second_max

print(Second_Max([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a python function to find the second smallest element in a list.
assert Second_Min([1,2,3]) == 1
"""

def Second_Min(l):
    min = l[0]
    second_min = l[0]
    for i in l:
        if i < min:
            second_min = min
            min = i
        elif i < second_min:
            second_min = i
    return second_min

print(Second_Min([1,2,3]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a python function to find the second largest element in a list.
assert Second_Max([