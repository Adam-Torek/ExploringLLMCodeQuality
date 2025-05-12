"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""

def is_woodall(num):
    # Convert the number to string
    num_str = str(num)
    # Check if the number has only digits
    if not num_str.isdigit():
        return False
    # Check if the number has 3 digits
    if len(num_str) != 3:
        return False
    # Check if the sum of the digits is equal to the number
    if sum(int(digit) for digit in num_str) != int(num_str):
        return False
    # Check if the number is divisible by 3
    if num % 3 != 0:
        return False
    # Check if the number is divisible by 5
    if num % 5 != 0:
        return False
    # Check if the number is divisible by 7
    if num % 7 != 0:
        return False
    # Check if the number is divisible by 9
    if num % 9 != 0:
        return False
    # Check if the number is divisible by 11
    if num % 11 != 0:
        return False
    # Check if the number is divisible by 13
    if num % 13 != 0:
        return False
    # Check if the number is divisible by 15
    if num % 15 != 0:
        return False
    # Check if the number is divisible by 17
    if num % 17 != 0:
        return False
    # Check if the number is divisible by 19
    if num % 19 != 0:
        return False
    # Check if the number is divisible by 23
    if num % 23 != 0:
        return False
    # Check if the number is divisible by 29
    if num % 29 != 0:
        return False
    # Check if the number is divisible by 31
    if num % 31 != 0:
        return False
    # Check if the number is divisible by 37
    if num % 37 != 0:
        return False
    # Check if the number is divisible by 41
    if num % 41 != 0:
        return False
    # Check if the number is divisible by 43
    if num % 43 != 0:
        return False
    # Check if the number is divisible by 47
    if num % 47 != 0:
        return False
    # Check if the number is divisible by 53
    if num % 53 != 0:
        return False
    # Check if the number is divisible by 59
    if num % 59 != 0:
        return False
    # Check if the number is divisible by 61
    if num % 61 != 0:
        return False
    # Check if the number is divisible by 67
    if num % 67 != 0:
        return False
    # Check if the number is divisible by 71
    if num % 71 != 0:
        return False
    # Check if the number is divisible by 73
    if num % 73 != 0:
        return False
    # Check if the number is divisible by 79
    if num % 79 != 0:
        return False
    # Check if the number is divisible by 83
    if num % 83 != 0:
        return False
    # Check if the number is divisible by 89
    if num % 89 != 0:
        return False
    # Check if the number is divisible by 97
    if num % 97 != 0:
        return False
    # Check if the number is divisible by 101
    if num % 101 != 0:
        return False
    # Check if the number is divisible by 103
    if num % 103 != 0:
        return False
    # Check if the number is divisible by 107
    if num % 107 != 0:
        return