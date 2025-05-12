"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    return [{} for i in range(n)]

print(empty_list(5))
/python/list_comprehension.py
"""
Write a function that takes a list of numbers and returns a new list with only the even numbers.
assert even_list([1,2,3,4,5,6]) == [2,4,6]
"""

def even_list(numbers):
    return [number for number in numbers if number % 2 == 0]

print(even_list([1,2,3,4,5,6]))
/python/list_comprehension_2.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd numbers.
assert odd_list([1,2,3,4,5,6]) == [1,3,5]
"""

def odd_list(numbers):
    return [number for number in numbers if number % 2!= 0]

print(odd_list([1,2,3,4,5,6]))
/python/list_comprehension_3.py
"""
Write a function that takes a list of numbers and returns a new list with only the positive numbers.
assert positive_list([-1,-2,-3,4,5,6]) == [4,5,6]
"""

def positive_list(numbers):
    return [number for number in numbers if number > 0]

print(positive_list([-1,-2,-3,4,5,6]))
/python/list_comprehension_4.py
"""
Write a function that takes a list of numbers and returns a new list with only the negative numbers.
assert negative_list([-1,-2,-3,4,5,6]) == [-1,-2,-3]
"""

def negative_list(numbers):
    return [number for number in numbers if number < 0]

print(negative_list([-1,-2,-3,4,5,6]))
/python/list_comprehension_5.py
"""
Write a function that takes a list of numbers and returns a new list with only the prime numbers.
assert prime_list([1,2,3,4,5,6]) == [2,3,5]
"""

def prime_list(numbers):
    return [number for number in numbers if number > 1 and all(number % i!= 0 for i in range(2, number))]

print(prime_list([1,2,3,4,5,6]))
/python/list_comprehension_6.py
"""
Write a function that takes a list of numbers and returns a new list with only the even prime numbers.
assert even_prime_list([1,2,3,4,5,6]) == [2,4]
"""

def even_prime_list(numbers):
    return [number for number in numbers if number > 1 and all(number % i!= 0 for i in range(2, number)) and number % 2 == 0]

print(even_prime_list([1,2,3,4,5,6]))
/python/list_comprehension_7.py
"""
Write a function that takes a list of numbers and returns a new list with only the odd prime numbers.
assert odd_prime_list([1,2,3,4,5,6]) == [3,5]
"""

def odd_prime_list(numbers):
    return [number for number in numbers if number > 1 and all(number % i!= 0 for i in range(2, number)) and number % 2!= 0]

print(odd_prime_list([1,2,3,4,5,6]))
/python/list_comprehension_8.py
"""
Write a function that takes a list of numbers and returns a new list with only the even prime numbers.
assert even_prime_list([1,2,3,4,5,6]) == [2,4]
"""

def even_prime_list(numbers):
    return [number for number in numbers if number > 1 and all(number % i!= 0 for i in range(2, number)) and number % 2 == 0]

print(even_prime_