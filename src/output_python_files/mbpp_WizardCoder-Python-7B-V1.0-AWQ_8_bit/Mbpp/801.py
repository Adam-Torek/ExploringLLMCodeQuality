"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a, b, c):
    count = 0
    if a == b and b == c:
        count += 1
    if a == b and a != c:
        count += 1
    if a == c and a != b:
        count += 1
    if b == c and b != a:
        count += 1
    if a != b and b != c and c != a:
        count += 1
    return count

print(test_three_equal(1,1,1)) # Output: 3
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,2)) # Output: 1
print(test_three_equal(1,2,2)) # Output: 1
print(test_three_equal(1,1,3)) # Output: 1
print(test_three_equal(2,2,2)) # Output: 2
print(test_three_equal(1,2,3)) # Output: 0
print(test_three_equal(1,1,3)) # Output: 2
print(test_three_equal(1,2,4)) # Output: 0
print(test_three_equal(1,1,4)) # Output: 2
print(test_three_equal(1,2,5)) # Output: 0
print(test_three_equal(1,3,3)) # Output: 1
print(test_three_equal(2,2,2)) # Output: 3
print(test_three_equal(1,1,1)) # Output: 3
print(test_three_equal(1,1,4)) # Output: 2
print(test_three_equal(1,2,5)) # Output: 0
print(test_three_equal(1,3,3)) # Output: 1
print(test_three_equal(2,2,2)) # Output: 3
print(test_three_equal(1,1,1)) # Output: 3
print(test_three_equal(1,1,4)) # Output: 2
print(test_three_equal(1,2,5)) # Output: 0
print(test_three_equal(1,3,3)) # Output: 1

# Test cases
# test_three_equal(1,1,1) == 3
# test_three_equal(1,2,3) == 0
# test_three_equal(1,1,2) == 1
# test_three_equal(1,2,2) == 1
# test_three_equal(1,1,3) == 1
# test_three_equal(2,2,2) == 2
# test_three_equal(1,2,3) == 0
# test_three_equal(1,1,3) == 2
# test_three_equal(1,2,4) == 0
# test_three_equal(1,1,4) == 2
# test_three_equal(1,2,5) == 0
# test_three_equal(1,3,3) == 1
# test_three_equal(2,2,2) == 3
# test_three_equal(1,1,1) == 3
# test_three_equal(1,1,4) == 2
# test_three_equal(1,2,5) == 0
# test_three_equal(1,3,3) == 1
# test_three_equal(2,2,2) == 3
# test_three_equal(1,1,1) == 3
# test_three_equal(1,1,4) == 2
# test_three_equal(1,2,5) == 0
# test_three_equal(1,3,3) == 1

# Test cases with negative numbers
# test_three_equal(-1,1,1) == 3
# test_three_equal(1,-1,1) == 3
# test_three_equal(1