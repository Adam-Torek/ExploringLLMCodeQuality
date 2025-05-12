"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a,b,c):
    if a == b == c:
        return 3
    elif a == b:
        return 2
    elif a == c:
        return 2
    elif b == c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1))
print(test_three_equal(1,1,2))
print(test_three_equal(1,2,2))
print(test_three_equal(1,2,3))
print(test_three_equal(1,3,3))
print(test_three_equal(2,2,3))
print(test_three_equal(2,3,3))
print(test_three_equal(3,3,3))
print(test_three_equal(1,2,4))
print(test_three_equal(1,3,4))
print(test_three_equal(1,4,4))
print(test_three_equal(2,3,4))
print(test_three_equal(2,4,4))
print(test_three_equal(3,4,4))
print(test_three_equal(1,2,5))
print(test_three_equal(1,3,5))
print(test_three_equal(1,4,5))
print(test_three_equal(1,5,5))
print(test_three_equal(2,3,5))
print(test_three_equal(2,4,5))
print(test_three_equal(2,5,5))
print(test_three_equal(3,4,5))
print(test_three_equal(3,5,5))
print(test_three_equal(4,5,5))
print(test_three_equal(1,2,6))
print(test_three_equal(1,3,6))
print(test_three_equal(1,4,6))
print(test_three_equal(1,5,6))
print(test_three_equal(1,6,6))
print(test_three_equal(2,3,6))
print(test_three_equal(2,4,6))
print(test_three_equal(2,5,6))
print(test_three_equal(2,6,6))
print(test_three_equal(3,4,6))
print(test_three_equal(3,5,6))
print(test_three_equal(3,6,6))
print(test_three_equal(4,5,6))
print(test_three_equal(4,6,6))
print(test_three_equal(5,6,6))
print(test_three_equal(1,2,7))
print(test_three_equal(1,3,7))
print(test_three_equal(1,4,7))
print(test_three_equal(1,5,7))
print(test_three_equal(1,6,7))
print(test_three_equal(1,7,7))
print(test_three_equal(2,3,7))
print(test_three_equal(2,4,7))
print(test_three_equal(2,5,7))
print(test_three_equal(2,6,7))
print(test_three_equal(2,7,7))
print(test_three_equal(3,4,7))
print(test_three_equal(3,5,7))
print(test_three_equal(3,6,7))
print(test_three_equal(3,7,7))
print(test_three_equal(4,5,7))
print(test_three_equal(4,6,7))
print(test_three_equal(4,7,7))
print(test_three_equal(5,6,7))
print(test_three_equal(5,7,7))
print(test_three_equal(6,7,7))
print(test_three_equal(1,2,8