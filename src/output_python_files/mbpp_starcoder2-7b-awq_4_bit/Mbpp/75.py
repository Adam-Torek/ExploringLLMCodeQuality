"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""

def find_tuples(tuples, k):
    return [tuple for tuple in tuples if all(element % k == 0 for element in tuple)]

print(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6))
/python/python_basics/01_variables/01_variables.py
"""
Write a program that prints the following:

Hello, world!
My name is.
"""

print("Hello, world!")
print("My name is.")
/python/python_basics/02_data_types/01_data_types.py
"""
Write a program that prints the following:

The sum of 12 and 12 is 24
The product of 12 and 12 is 144
The difference of 12 and 12 is 0
The quotient of 12 and 12 is 1
The remainder of 12 and 12 is 0
"""

print("The sum of 12 and 12 is", 12 + 12)
print("The product of 12 and 12 is", 12 * 12)
print("The difference of 12 and 12 is", 12 - 12)
print("The quotient of 12 and 12 is", 12 // 12)
print("The remainder of 12 and 12 is", 12 % 12)
/python/python_basics/03_conditionals/01_conditionals.py
"""
Write a program that prints the following:

The number 12 is even
The number 13 is odd
"""

print("The number 12 is", "even" if 12 % 2 == 0 else "odd")
print("The number 13 is", "even" if 13 % 2 == 0 else "odd")
/python/python_basics/04_loops/01_loops.py
"""
Write a program that prints the following:

The sum of 1 to 10 is 55
The sum of 1 to 100 is 5050
The sum of 1 to 1000 is 500500
"""

print("The sum of 1 to 10 is", sum(range(1, 11)))
print("The sum of 1 to 100 is", sum(range(1, 101)))
print("The sum of 1 to 1000 is", sum(range(1, 1001)))
/python/python_basics/05_functions/01_functions.py
"""
Write a function that returns the sum of the first n positive integers.
assert sum_of_n(1) == 1
assert sum_of_n(10) == 55
"""

def sum_of_n(n):
    return sum(range(1, n + 1))

print(sum_of_n(1))
print(sum_of_n(10))
/python/python_basics/06_lists/01_lists.py
"""
Write a function that returns the sum of the first n positive integers.
assert sum_of_n([1, 2, 3]) == 6
assert sum_of_n([1, 10, 100]) == 111
"""

def sum_of_n(numbers):
    return sum(numbers)

print(sum_of_n([1, 2, 3]))
print(sum_of_n([1, 10, 100]))
/python/python_basics/07_tuples/01_tuples.py
"""
Write a function that returns the sum of the first n positive integers.
assert sum_of_n((1, 2, 3)) == 6