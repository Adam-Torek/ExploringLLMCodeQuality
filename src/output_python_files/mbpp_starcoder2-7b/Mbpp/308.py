"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""
def large_product(list1,list2,n):
    list1.sort()
    list2.sort()
    list1.reverse()
    list2.reverse()
    list3=[]
    for i in range(n):
        list3.append(list1[i]*list2[i])
    return list3

print(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_1.py
"""
Write a function that takes a list of numbers and returns the largest number in the list.
assert largest([1,2,3,4,5])==5
"""
def largest(list):
    list.sort()
    return list[-1]

print(largest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_3.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_4.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2,3,4,5])==1
"""
def smallest(list):
    list.sort()
    return list[0]

print(smallest([1,2,3,4,5]))
/Python/Python_Basics/Python_Basics_2/Python_Basics_2_5.py
"""
Write a function that takes a list of numbers and returns the smallest number in the list.
assert smallest([1,2