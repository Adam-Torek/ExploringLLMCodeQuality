"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""

def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))

print(multiply_elements((1, 5, 7, 8, 10)))
/week01/day04/01_sum_of_digits.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(2019) == 2 + 0 + 1 + 9 == 12
"""

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(2019))
/week01/day04/02_sum_of_digits_2.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(2019) == 2 + 0 + 1 + 9 == 12
"""

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(2019))

def sum_of_digits_2(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_2(2019))
/week01/day04/03_sum_of_digits_3.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(2019) == 2 + 0 + 1 + 9 == 12
"""

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(2019))

def sum_of_digits_2(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_2(2019))

def sum_of_digits_3(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_3(2019))
/week01/day04/04_sum_of_digits_4.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(2019) == 2 + 0 + 1 + 9 == 12
"""

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(2019))

def sum_of_digits_2(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_2(2019))

def sum_of_digits_3(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_3(2019))

def sum_of_digits_4(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_4(2019))
/week01/day04/05_sum_of_digits_5.py
"""
Write a function that takes a number and returns the sum of its digits.
assert sum_of_digits(2019) == 2 + 0 + 1 + 9 == 12
"""

def sum_of_digits(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits(2019))

def sum_of_digits_2(n):
    return sum(int(i) for i in str(n))

print(sum_of_digits_2(