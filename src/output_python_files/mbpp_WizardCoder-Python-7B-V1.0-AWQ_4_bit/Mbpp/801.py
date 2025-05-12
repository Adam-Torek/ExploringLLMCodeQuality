"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a, b, c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1)) # Output: 3
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,2)) # Output: 2
print(test_three_equal(1,2,2)) # Output: 1
print(test_three_equal(1,3,3)) # Output: 1
print(test_three_equal(2,2,2)) # Output: 3
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,3)) # Output: 2
print(test_three_equal(1,3,2)) # Output: 1
print(test_three_equal(2,1,3)) # Output: 1
print(test_three_equal(2,3,2)) # Output: 1
print(test_three_equal(3,2,1)) # Output: 1
print(test_three_equal(3,3,3)) # Output: 3