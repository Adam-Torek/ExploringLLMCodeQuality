"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""

def last_Digit(num):
    return num % 10

print(last_Digit(123)) # Output: 3
print(last_Digit(456)) # Output: 6
print(last_Digit(789)) # Output: 9