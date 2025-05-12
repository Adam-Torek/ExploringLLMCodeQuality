"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""

def sum_list(list1,list2):
    return [list1[i]+list2[i] for i in range(len(list1))]

print(sum_list([10,20,30],[15,25,35]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
"""

def max_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

print(max_list([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function that takes a list of numbers and returns a list where the first element is the largest number, the second element is the second largest number in the list and so on.
"""

def max_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def sort_list(list):
    sorted_list = []
    for i in range(len(list)):
        sorted_list.append(max_list(list))
        list.remove(max_list(list))
    return sorted_list

print(sort_list([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes a list of numbers and returns a list where the first element is the smallest number, the second element is the second smallest number in the list and so on.
"""

def min_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def sort_list(list):
    sorted_list = []
    for i in range(len(list)):
        sorted_list.append(min_list(list))
        list.remove(min_list(list))
    return sorted_list

print(sort_list([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function that takes a list of numbers and returns a list where the first element is the smallest number, the second element is the second smallest number in the list and so on.
"""

def min_list(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def sort_list(list):
    sorted_list = []
    for i in range(len(list)):
        sorted_list.append(min_list(list))
        list.remove(min_list(list))
    return sorted_list

def max_list(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def sort_list(list):
    sorted_list = []
    for i in range(len(list)):
        sorted_list.append(max_list(list))
        list.remove(max_list(list))
    return sorted_list

print(sort_list([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a function that takes a list of numbers and returns a list where the first element is the smallest number, the second element is the second smallest number in the list and so on.
"""

def min_list(list):