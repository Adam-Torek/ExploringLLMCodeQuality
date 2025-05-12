"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""

def first_Digit(num):
    return int(str(num)[0])

print(first_Digit(123)) # Output: 1
print(first_Digit(456)) # Output: 4
print(first_Digit(789)) # Output: 7
print(first_Digit(1000)) # Output: 1
print(first_Digit(0) # Output: 0