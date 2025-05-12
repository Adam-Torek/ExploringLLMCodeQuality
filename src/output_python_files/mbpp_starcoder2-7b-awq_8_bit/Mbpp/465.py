"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""

def drop_empty(d):
    return {k:v for k,v in d.items() if v}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))
/python/python_basics/python_basics_001.py
"""
Write a function to find the longest word in a given list of words.
assert longest_word(['Hello', 'World', 'In', 'Python'])=='Python'
"""

def longest_word(words):
    return max(words, key=len)

print(longest_word(['Hello', 'World', 'In', 'Python']))
/python/python_basics/python_basics_005.py
"""
Write a function to find the median of a given list of integers.
assert median([1,2,3,4,5])==3
"""

def median(numbers):
    numbers.sort()
    return numbers[len(numbers)//2]

print(median([1,2,3,4,5]))
/python/python_basics/python_basics_002.py
"""
Write a function to find the second largest word in a given list of words.
assert second_largest(['Hello', 'World', 'In', 'Python'])=='World'
"""

def second_largest(words):
    words.sort(reverse=True)
    return words[1]

print(second_largest(['Hello', 'World', 'In', 'Python']))
/python/python_basics/python_basics_003.py
"""
Write a function to find the second smallest word in a given list of words.
assert second_smallest(['Hello', 'World', 'In', 'Python'])=='In'
"""

def second_smallest(words):
    words.sort()
    return words[1]

print(second_smallest(['Hello', 'World', 'In', 'Python']))
/python/python_basics/python_basics_004.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/python_basics_006.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/python_basics_007.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/python_basics_008.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/python_basics_009.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,4,5])==15
"""

def sum_of_numbers(numbers):
    return sum(numbers)

print(sum_of_numbers([1,2,3,4,5]))
/python/python_basics/python_basics_010.py
"""
Write a function to find the sum of the given list of numbers.
assert sum_of_numbers([1,2,3,