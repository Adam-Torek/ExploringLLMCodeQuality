"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(num1, num2, num3):
    count = 0
    if num1 == num2 and num1 == num3:
        count = 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        count = 2
    return count

# Test the function
assert test_three_equal(1,1,1) == 3
assert test_three_equal(1,1,2) == 2
assert test_three_equal(1,2,1) == 2
assert test_three_equal(1,2,2) == 1
assert test_three_equal(2,2,2) == 3
assert test_three_equal(3,3,3) == 3</s>