"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a,b,c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1))
print(test_three_equal(1,1,2))
print(test_three_equal(1,2,3))
print(test_three_equal(1,2,2))
print(test_three_equal(1,2,1))
print(test_three_equal(1,1,3))
print(test_three_equal(1,3,3))
print(test_three_equal(3,3,3))
print(test_three_equal(1,2,4))
print(test_three_equal(1,4,4))
print(test_three_equal(4,4,4))
print(test_three_equal(1,1,1))
print(test_three_equal(1,1,2))
print(test_three_equal(1,2,3))
print(test_three_equal(1,2,2))
print(test_three_equal(1,2,1))
print(test_three_equal(1,1,3))
print(test_three_equal(1,3,3))
print(test_three_equal(3,3,3))
print(test_three_equal(1,2,4))
print(test_three_equal(1,4,4))
print(test_three_equal(4,4,4))
<file_sep>/python/python_basics/python_basics_001.py
"""
Write a python function to check whether a given number is even or odd.
"""

def test_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(test_even_odd(1))
print(test_even_odd(2))
print(test_even_odd(3))
print(test_even_odd(4))
print(test_even_odd(5))
print(test_even_odd(6))
print(test_even_odd(7))
print(test_even_odd(8))
print(test_even_odd(9))
print(test_even_odd(10))
print(test_even_odd(11))
print(test_even_odd(12))
print(test_even_odd(13))
print(test_even_odd(14))
print(test_even_odd(15))
print(test_even_odd(16))
print(test_even_odd(17))
print(test_even_odd(18))
print(test_even_odd(19))
print(test_even_odd(20))
print(test_even_odd(21))
print(test_even_odd(22))
print(test_even_odd(23))
print(test_even_odd(24))
print(test_even_odd(25))
print(test_even_odd(26))
print(test_even_odd(27))
print(test_even_odd(28))
print(test_even_odd(29))
print(test_even_odd(30))
print(test_even_odd(31))
print(test_even_odd(32))
print(test_even_odd(33))
print(test_even_odd(34))
print(test_even_odd(35))
print(test_even_odd(36))
print(test_even_odd(37))
print(test_even_odd(38))
print(test_even_odd(39))
print(test_even_odd(40))
print(test_even_odd(41))
print(test_even_odd(42))
print(test_even_odd(43))
print(test_even_odd(44))
print(test_even_odd(45))