"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""
def find_Max_Num(digits):
    # Convert the list to a string and convert it to integer
    max_num = int(''.join(str(digit) for digit in digits)[::-1])
    return max_num

# Test the function
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6]) == 654
assert find_Max_Num([7,8,9]) == 987
assert find_Max_Num([0,0,0]) == 000
assert find_Max_Num([]) == 0