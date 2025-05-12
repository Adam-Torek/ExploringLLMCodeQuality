"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""

def removezero_ip(ip):
    ip = ip.split('.')
    ip = [str(int(i)) for i in ip]
    ip = '.'.join(ip)
    return ip

print(removezero_ip("216.08.094.196"))
/python/python_practice/python_practice_1.py
"""
Write a function that takes a list of numbers and returns the sum of the numbers.
assert sum_list([1,2,3,4])==10
"""

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list([1,2,3,4]))
/python/python_practice/python_practice_10.py
"""
Write a function that takes a list and returns a new list with unique elements of the first list.
assert unique_list([1,2,3,3,3,3,4,5])==[1,2,3,4,5]
"""

def unique_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique_list([1,2,3,3,3,3,4,5]))
/python/python_practice/python_practice_11.py
"""
Write a function that takes a list and returns a new list with the elements of the first list in reverse order.
assert reverse_list([1,2,3,4])==[4,3,2,1]
"""

def reverse_list(list):
    new_list = []
    for i in range(len(list)-1,-1,-1):
        new_list.append(list[i])
    return new_list

print(reverse_list([1,2,3,4]))
/python/python_practice/python_practice_12.py
"""
Write a function that takes a number and returns a list of its digits.
assert digit_list(123)==[1,2,3]
"""

def digit_list(number):
    new_list = []
    for i in str(number):
        new_list.append(int(i))
    return new_list

print(digit_list(123))
/python/python_practice/python_practice_13.py
"""
Write a function that takes a list and returns a new list with only odd numbers of the first list.
assert odd_list([1,2,3,4,5,6])==[1,3,5]
"""

def odd_list(list):
    new_list = []
    for i in list:
        if i%2!= 0:
            new_list.append(i)
    return new_list

print(odd_list([1,2,3,4,5,6]))
/python/python_practice/python_practice_14.py
"""
Write a function that takes a list and returns a new list with only the even numbers of the first list.
assert even_list([1,2,3,4,5,6])==[2,4,6]
"""

def even_list(list):
    new_list = []
    for i in list:
        if i%2 == 0:
            new_list.append(i)
    return new_list

print(even_list([1,2,3,4,5,6]))
/python/python_practice/python_practice_15.py
"""
Write a function that takes a list and returns a new list with the elements of the first list except for the
indices 0 and len(list)-1.
assert except_first_last([1,2,3,4])==[2,3]
"""

def except_first_last(list):
    new_list = []
    for i in range(1,len(list)-1):
        new_list.append(list[i])
    return new_list

print(except_first_last([1,2,3,4]))
/