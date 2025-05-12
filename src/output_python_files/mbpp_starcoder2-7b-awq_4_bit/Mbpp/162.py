"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""

def sum_series(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

print(sum_series(6))
/python/python_fundamentals/fundamentals/fundamentals_1/fundamentals_1_1.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1,2,1,2,3,3]) == [1,2,3]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1,2,1,2,3,3]))
/python/python_fundamentals/fundamentals/fundamentals_1/fundamentals_1_2.py
"""
Write a function that takes a number and returns a list of its digits.
assert digit_list(123) == [1,2,3]
"""

def digit_list(number):
    new_list = []
    for i in str(number):
        new_list.append(int(i))
    return new_list

print(digit_list(123))
/python/python_fundamentals/fundamentals/fundamentals_1/fundamentals_1_3.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1,2,1,2,3,3]) == [1,2,3]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def digit_list(number):
    new_list = []
    for i in str(number):
        new_list.append(int(i))
    return new_list

def sum_series(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

print(sum_series(6))
/python/python_fundamentals/fundamentals/fundamentals_1/fundamentals_1_4.py
"""
Write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
assert remove_duplicates([1,2,1,2,3,3]) == [1,2,3]
"""

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def digit_list(number):
    new_list = []
    for i in str(number):
        new_list.append(int(i))
    return new_list

def sum_series(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

def sum_series_2(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

def sum_series_3(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

def sum_series_4(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

def sum_series_5(n):
    sum = 0
    for i in range(0, n//2 + 1):
        sum += n - 2*i
    return sum

def sum_series_6(n):
    sum = 0
    for i in range(0, n//2