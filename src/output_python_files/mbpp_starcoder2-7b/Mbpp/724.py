"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""

def power_base_sum(base, power):
    return sum([int(i) for i in str(base**power)])

print(power_base_sum(2,100))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_digits(10)  # Returns 1
sum_of_digits(99)  # Returns 18
sum_of_digits(-32) # Returns 5
"""

def sum_of_digits(n):
    return sum([abs(int(i)) for i in str(n)])

print(sum_of_digits(10))
print(sum_of_digits(99))
print(sum_of_digits(-32))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits_2.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_digits(10)  # Returns 1
sum_of_digits(99)  # Returns 18
sum_of_digits(-32) # Returns 5
"""

def sum_of_digits(n):
    return sum(abs(int(i)) for i in str(n))

print(sum_of_digits(10))
print(sum_of_digits(99))
print(sum_of_digits(-32))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits_3.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_digits(10)  # Returns 1
sum_of_digits(99)  # Returns 18
sum_of_digits(-32) # Returns 5
"""

def sum_of_digits(n):
    return sum(map(abs, map(int, str(n))))

print(sum_of_digits(10))
print(sum_of_digits(99))
print(sum_of_digits(-32))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits_4.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_digits(10)  # Returns 1
sum_of_digits(99)  # Returns 18
sum_of_digits(-32) # Returns 5
"""

def sum_of_digits(n):
    return sum(map(abs, map(int, str(n))))

print(sum_of_digits(10))
print(sum_of_digits(99))
print(sum_of_digits(-32))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits_5.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_digits(10)  # Returns 1
sum_of_digits(99)  # Returns 18
sum_of_digits(-32) # Returns 5
"""

def sum_of_digits(n):
    return sum(map(abs, map(int, str(n))))

print(sum_of_digits(10))
print(sum_of_digits(99))
print(sum_of_digits(-32))
<file_sep>/Python/CodeWars/7kyu/Sum of Digits/sum_of_digits_6.py
"""
Write a function that takes an integer as input, and returns the sum of the absolute value of each of the digits of that number.
For example:

sum_of_