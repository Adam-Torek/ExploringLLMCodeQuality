"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    """
    This function takes a list of digits as an input and returns the maximum number that can be formed using those digits.
    """
    digits_set = set(digits)
    digits_set.remove(0)
    digits_list = list(digits_set)
    digits_list.sort()
    max_num = 0
    for i in range(len(digits_list)):
        for j in range(i+1,len(digits_list)):
            num = int(''.join(digits_list[i:j+1]))
            if num > max_num:
                max_num = num
    return max_num

# Test the function
assert find_Max_Num([1,2,3]) == 321
assert find_Max_Num([4,5,6,7,8,9]) == 987654321
assert find_Max_Num([0,1,2,3,4,5,6,7,8,9]) == 987654321
assert find_Max_Num([1,2,3,4,5,6,7,8,9,0]) == 987654321