"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a,b,c):
    count = 0
    if a == b == c:
        count += 1
    if a != b and b == c:
        count += 1
    if a == b and b != c:
        count += 1
    if a != b and a == c:
        count += 1
    if a != b and b != c and a == c:
        count += 1
    return count

print(test_three_equal(1,1,1)) # Output: 3
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,2)) # Output: 2
print(test_three_equal(1,2,2)) # Output: 1
print(test_three_equal(1,2,1)) # Output: 2
print(test_three_equal(1,1,3)) # Output: 2
print(test_three_equal(2,2,2)) # Output: 3
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,3)) # Output: 2
print(test_three_equal(1,2,2)) # Output: 1
print(test_three_equal(1,3,3)) # Output: 1
print(test_three_equal(2,2,2)) # Output: 3
print(test_three_equal(1,1,4)) # Output: 1
print(test_three_equal(1,2,4)) # Output: 1
print(test_three_equal(1,3,4)) # Output: 1
print(test_three_equal(2,2,4)) # Output: 1
print(test_three_equal(1,1,5)) # Output: 1
print(test_three_equal(1,2,5)) # Output: 1
print(test_three_equal(1,3,5)) # Output: 1
print(test_three_equal(2,2,5)) # Output: 1
print(test_three_equal(1,1,6)) # Output: 1
print(test_three_equal(1,2,6)) # Output: 1
print(test_three_equal(1,3,6)) # Output: 1
print(test_three_equal(2,2,6)) # Output: 1
print(test_three_equal(1,1,7)) # Output: 1
print(test_three_equal(1,2,7)) # Output: 1
print(test_three_equal(1,3,7)) # Output: 1
print(test_three_equal(2,2,7)) # Output: 1
print(test_three_equal(1,1,8)) # Output: 1
print(test_three_equal(1,2,8)) # Output: 1
print(test_three_equal(1,3,8)) # Output: 1
print(test_three_equal(2,2,8)) # Output: 1
print(test_three_equal(1,1,9)) # Output: 1
print(test_three_equal(1,2,9)) # Output: 1
print(test_three_equal(1,3,9)) # Output: 1
print(test_three_equal(2,2,9)) # Output: 1
print(test_three_equal(1,1,10)) # Output: 1
print(test_three_equal(1,2,10)) # Output: 1
print(test_three_equal(1,3,10)) # Output: 1
print(test_three_equal(2,2,10)) # Output: 1
print(test_three_equal(1,1,11)) # Output: 1
print(test_three_equal(1,2,11)) # Output: 1
print(test_three_equal(1,3,11)) # Output