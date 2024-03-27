"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""

def validate(num):
    freq = [0] * 10
    for digit in str(num):
        freq[int(digit)] += 1
    for digit in freq:
        if digit > num // digit:
            return False
    return True

# Test cases
print(validate(1234))  # True
print(validate(12345))  # False
print(validate(123456))  # True
print(validate(1234567))  # False
print(validate(123456789))  # True<|endoftext|>