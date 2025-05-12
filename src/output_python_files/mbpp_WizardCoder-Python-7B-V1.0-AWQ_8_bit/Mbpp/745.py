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

# Test cases
assert divisible_by_digits(1,22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(10,50) == [10, 20, 30, 40, 50]
assert divisible_by_digits(100,200) == [100, 200]
assert divisible_by_digits(1000,300) == [100, 200, 300]
assert divisible_by_digits(10000,20000) == [1000, 2000, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
assert divisible_by_digits(10000,30000) == [1000, 2000, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3000]
assert divisible_by_digits(100000,200000) == [10000, 20000, 30000, 40000, 50000, 60000, 70000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
assert divisible_by_digits(1000000,2000000) == [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 120000, 130000, 140000, 1500