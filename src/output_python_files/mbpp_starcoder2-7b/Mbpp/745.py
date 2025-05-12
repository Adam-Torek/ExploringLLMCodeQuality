"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

def divisible_by_digits(startnum, endnum):
    return [i for i in range(startnum, endnum+1) if all(i%int(j) == 0 for j in str(i))]

print(divisible_by_digits(1,22))
/python/python_exercises/python_lambda_exercise_18.py
"""
Write a function to find the maximum and minimum numbers from a sequence of numbers. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-18.php
assert max_min([1,2,3,4,5]) == (5,1)
"""

def max_min(seq):
    return (max(seq), min(seq))

print(max_min([1,2,3,4,5]))
/python/python_exercises/python_lambda_exercise_11.py
"""
Write a function to find the sum of the series 1 + 1/2 + 1/3 + 1/4 +... + 1/n. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-11.php
assert sum_series(4) == 1.8333333333333333
"""

def sum_series(n):
    return sum(1/i for i in range(1, n+1))

print(sum_series(4))
/python/python_exercises/python_lambda_exercise_23.py
"""
Write a function to find the sum of the series 1 + 1/2^2 + 1/3^2 + 1/4^2 +... + 1/n^2. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-23.php
assert sum_series(4) == 1.6875
"""

def sum_series(n):
    return sum(1/(i**2) for i in range(1, n+1))

print(sum_series(4))
/python/python_exercises/python_lambda_exercise_16.py
"""
Write a function to find the sum of the series 1 + 1/2 + 1/3 + 1/4 +... + 1/n. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-16.php
assert sum_series(4) == 2.75
"""

def sum_series(n):
    return sum(1/i for i in range(1, n+1))

print(sum_series(4))
/python/python_exercises/python_lambda_exercise_15.py
"""
Write a function to find the sum of the series 1 + 1/2 + 1/3 + 1/4 +... + 1/n. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-15.php
assert sum_series(4) == 2.25
"""

def sum_series(n):
    return sum(1/i for i in range(1, n+1))

print(sum_series(4))
/python/python_exercises/python_lambda_exercise_19.py
"""
Write a function to find the sum of the series 1 + 1/2 + 1/3 + 1/4 +... + 1/n. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-19.php
assert sum_series(4) == 2.25
"""

def sum_series(n):
    return sum(1/i for i in range(1, n+1))

print(sum_series(4))
/python/python