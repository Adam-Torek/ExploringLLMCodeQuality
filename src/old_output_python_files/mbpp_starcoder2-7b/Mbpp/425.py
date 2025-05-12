"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(list_of_lists,element):
    count=0
    for i in list_of_lists:
        if element in i:
            count+=1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1))
<file_sep>/python_basics/python_basics_1/python_basics_1_1.py
"""
Write a function to find the maximum element in a list.
assert find_max([1, 3, 5, 7, 9])==9
"""
def find_max(list_of_numbers):
    max_number=list_of_numbers[0]
    for i in list_of_numbers:
        if i>max_number:
            max_number=i
    return max_number

print(find_max([1, 3, 5, 7, 9]))
<file_sep>/python_basics/python_basics_1/python_basics_1_2.py
"""
Write a function to find the minimum element in a list.
assert find_min([1, 3, 5, 7, 9])==1
"""
def find_min(list_of_numbers):
    min_number=list_of_numbers[0]
    for i in list_of_numbers:
        if i<min_number:
            min_number=i
    return min_number

print(find_min([1, 3, 5, 7, 9]))
<file_sep>/python_basics/python_basics_1/python_basics_1_3.py
"""
Write a function to find the sum of all the elements in a list.
assert find_sum([1, 3, 5, 7, 9])==25
"""
def find_sum(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum

print(find_sum([1, 3, 5, 7, 9]))
<file_sep>/python_basics/python_basics_1/python_basics_1_4.py
"""
Write a function to find the average of all the elements in a list.
assert find_average([1, 3, 5, 7, 9])==5
"""
def find_average(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum/len(list_of_numbers)

print(find_average([1, 3, 5, 7, 9]))
<file_sep>/python_basics/python_basics_1/python_basics_1_5.py
"""
Write a function to find the average of all the elements in a list.
assert find_average([1, 3, 5, 7, 9])==5
"""
def find_average(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum/len(list_of_numbers)

print(find_average([1, 3, 5, 7, 9]))

"""
Write a function to find the average of all the elements in a list.
assert find_average([1, 3, 5, 7, 9])==5
"""
def find_average(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum/len(list_of_numbers)

print(find_average([1, 3, 5, 7, 9]))

"""
Write a function to find the average of all the elements in a list.
assert find_average([1, 3, 5, 7, 9])==5
"""
def find_average(list_of_numbers):
    sum=0
    for i in list_of_numbers:
        sum+=i
    return sum/len(list_of_numbers)

print(find_average([1, 3, 5, 7, 9]))

"""
Write a function to find the average of all