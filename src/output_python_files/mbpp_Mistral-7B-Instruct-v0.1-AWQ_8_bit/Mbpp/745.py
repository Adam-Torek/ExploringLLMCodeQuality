"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-24.php
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

def divisible_by_digits(startnum, endnum):
    """
    Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains.
    """
    digits = [int(digit) for digit in str(startnum)]
    for num in range(startnum, endnum+1):
        digits2 = [int(digit) for digit in str(num)]
        if all(digit%digit2 == 0 for digit, digit2 in zip(digits, digits2)):
            yield num


if __name__ == '__main__':
    print(list(divisible_by_digits(1, 22)))