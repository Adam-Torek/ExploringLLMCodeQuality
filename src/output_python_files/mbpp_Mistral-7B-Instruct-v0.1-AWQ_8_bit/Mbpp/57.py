"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    """
    This function takes a list of digits as an input and returns the largest number that can be formed using those digits.
    """
    digits = sorted(digits, reverse=True)
    num = 0
    for digit in digits:
        num = num*10 + digit
    return num

# Test the function
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,7,8,9]) == 987654321
assert find_Max_Num([0,0,0,0,0,0]) == 0
assert find_Max_Num([9,8,7,6,5,4,3,2,1]) == 987654321