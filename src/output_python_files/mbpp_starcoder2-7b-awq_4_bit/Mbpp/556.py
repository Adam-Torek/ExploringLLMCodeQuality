"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] ^ arr[j]) % 2!= 0:
                count += 1
    return count

print(find_Odd_Pair([5,4,7,2,1],5))/Python/Python_Basics/Python_Basics_1.py
"""
Write a python function to find the sum of the digits of a given number.
assert sum_digits(123) == 6
"""

def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

print(sum_digits(123))/Python/Python_Basics/Python_Basics_10.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(count_digits(123))/Python/Python_Basics/Python_Basics_12.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_11.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(count_digits(123))/Python/Python_Basics/Python_Basics_13.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_14.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_15.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_16.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_17.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_18.py
"""
Write a python function to find the number of digits in a given number.
assert count_digits(123) == 3
"""

def count_digits(n):
    return len(str(n))

print(count_digits(123))/Python/Python_Basics/Python_Basics_19.py
"""
Write a python function to find the number of digits in a given number