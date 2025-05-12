"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""

def get_total_number_of_sequences(m, n):
    if n == 1:
        return 1
    elif n == 2:
        return min(m, 2)
    else:
        return get_total_number_of_sequences(m, n-1) + get_total_number_of_sequences(m, n-2)

print(get_total_number_of_sequences(10, 4))
/recursion/get_permutations.py
"""
Write a function that takes in a string of characters and returns all permutations of the string.
assert get_permutations("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
"""

def get_permutations(string):
    if len(string) == 1:
        return [string]
    else:
        permutations = []
        for i in range(len(string)):
            for permutation in get_permutations(string[:i] + string[i+1:]):
                permutations.append(string[i] + permutation)
        return permutations

print(get_permutations("abc"))
/recursion/get_power.py
"""
Write a function that takes in a base and an exponent and returns the power of the base to the exponent.
assert get_power(2, 3) == 8
"""

def get_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * get_power(base, exponent-1)

print(get_power(2, 3))
/recursion/get_fibonacci.py
"""
Write a function that takes in a number and returns the nth number of the fibonacci sequence.
assert get_fibonacci(5) == 5
"""

def get_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

print(get_fibonacci(5))
/recursion/get_factorial.py
"""
Write a function that takes in a number and returns the factorial of the number.
assert get_factorial(5) == 120
"""

def get_factorial(n):
    if n == 1:
        return 1
    else:
        return n * get_factorial(n-1)

print(get_factorial(5))
/recursion/get_product_of_array.py
"""
Write a function that takes in an array of numbers and returns the product of all the numbers in the array.
assert get_product_of_array([1, 2, 3]) == 6
"""

def get_product_of_array(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] * get_product_of_array(array[1:])

print(get_product_of_array([1, 2, 3]))
/recursion/get_max_number.py
"""
Write a function that takes in an array of numbers and returns the maximum number in the array.
assert get_max_number([1, 2, 3]) == 3
"""

def get_max_number(array):
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], get_max_number(array[1:]))

print(get_max_number([1, 2, 3]))
/recursion/get_min_number.py
"""
Write a function that takes in an array of numbers and returns the minimum number in the array.
assert get_min_number([1, 2, 3]) == 1
"""

def get_min_number(array):
    if len(array) == 1:
        return array[0]
    else:
        return min(array[0], get_min_number(array[1:]))

print(get_min_number([1, 2, 3]))
/recursion/get_sum_of