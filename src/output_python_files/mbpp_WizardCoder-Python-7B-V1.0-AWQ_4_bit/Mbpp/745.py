"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

def divisible_by_digits(startnum, endnum):
    def is_divisible(num):
        for digit in str(num):
            if num % int(digit) != 0:
                return False
        return True

    return [num for num in range(startnum, endnum+1) if is_divisible(num)]

print(divisible_by_digits(1,22)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]