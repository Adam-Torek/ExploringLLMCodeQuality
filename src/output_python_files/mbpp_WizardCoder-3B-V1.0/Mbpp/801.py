"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""

def test_three_equal(a, b, c):
    count = 0
    for i in range(a, b+1):
        if i == a or i == b or i == c:
            count += 1
    return count

# Test cases
assert test_three_equal(1,1,1) == 3
assert test_three_equal(1,2,3) == 0
assert test_three_equal(1,3,2) == 0
assert test_three_equal(1,2,2) == 1
assert test_three_equal(1,2,3) == 2
assert test_three_equal(1,3,1) == 1
assert test_three_equal(1,3,2) == 2
assert test_three_equal(1,3,3) == 3<|endoftext|>