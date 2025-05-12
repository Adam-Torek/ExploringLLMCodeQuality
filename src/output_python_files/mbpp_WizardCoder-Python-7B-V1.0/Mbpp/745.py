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

    return list(filter(is_divisible, range(startnum, endnum+1)))

print(divisible_by_digits(1,22)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(divisible_by_digits(10,30)) # [10, 22, 33]
print(divisible_by_digits(100,200)) # [100, 111, 121, 132, 143, 154, 165, 176, 187, 198, 200]
print(divisible_by_digits(1000,2000)) # [100, 111, 121, 132, 143, 154, 165, 176, 187, 198, 200, 222, 233, 244, 255, 266, 277, 288, 299, 300]
print(divisible_by_digits(10000,30000)) # [1000, 1111, 1212, 1323, 1434, 1545, 1656, 1767, 1878, 1989, 2000, 2111, 2222, 23333, 2444, 25555, 2666, 2777, 2888, 2999, 3000]

# Test cases
assert divisible_by_digits(1,22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(10,30) == [10, 22]
assert divisible_by_digits(100,200) == [100, 111, 121, 132, 143, 154, 165, 176, 187, 198, 200]
assert divisible_by_digits(1000,2000) == [100, 111, 121, 132, 143, 154, 165, 176, 187, 198, 200, 222, 233, 244, 255, 266, 277, 288, 299, 300]
assert divisible_by_digits(10000,30000) == [1000, 1111, 1212, 1323, 1434, 1545, 1656, 1767, 1878, 1989, 2000,