"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""

def convert_list_dictionary(list1,list2,list3):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for i in range(len(list1)):
        dict1[list1[i]] = list2[i]
        dict2[list1[i]] = list3[i]
    dict3[dict1] = dict2
    return dict3

print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92]))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a function to calculate the sum of the two given integers. If the two values are the same, then return triple their sum.
assert sum_of_two(3, 2) == 5
assert sum_of_two(3, 3) == 18
"""

def sum_of_two(a,b):
    if a == b:
        return (a+b)*3
    else:
        return a+b

print(sum_of_two(3,2))
print(sum_of_two(3,3))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a function to check whether a given integer is within 100 of 1000.
assert near_thousand(1000) == True
assert near_thousand(900) == True
assert near_thousand(800) == False
"""

def near_thousand(n):
    return (abs(1000-n) <= 100)

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a function to check whether a given positive number is a multiple of 3 or a multiple of 7.
assert multiple_of_three_or_seven(9) == True
assert multiple_of_three_or_seven(8) == False
"""

def multiple_of_three_or_seven(n):
    return (n%3 == 0 or n%7 == 0)

print(multiple_of_three_or_seven(9))
print(multiple_of_three_or_seven(8))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
assert sum_of_cubes(3) == 27
assert sum_of_cubes(5) == 225
"""

def sum_of_cubes(n):
    sum = 0
    for i in range(n):
        sum += i**3
    return sum

print(sum_of_cubes(3))
print(sum_of_cubes(5))
/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
assert sum_of_cubes(3) == 27
assert sum_of_cubes(5) == 225
"""

def sum_