"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    max_num = 0
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            for k in range(j+1, len(digits)):
                max_num = max(max_num, digits[i]*1000 + digits[j]*100 + digits[k])
    return max_num

# Test the function
assert find_Max_Num([1,2,3]) == 321<|endoftext|>