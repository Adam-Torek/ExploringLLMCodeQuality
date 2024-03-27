"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_Primes_nums(100))
<file_sep>/Python/Python_Basics/Python_Basics_1.py
"""
Write a python function that takes in a string and returns the number of vowels in the string.
assert count_vowels("hello") == 2
"""

def count_vowels(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_4.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_2.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_3.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_5.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_6.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_7.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_8.py
"""
Write a python function that takes in a string and returns the number of times the letter 'a' appears in the string.
assert count_a("hello") == 1
"""

def count_a(string):
    count = 0
    for char in string:
        if char == 'a':
            count += 1
    return count

print(count_a("hello"))
<file_sep>/Python/Python_Basics/Python_Basics_9.py
"""
Write a python function that takes in a string and returns