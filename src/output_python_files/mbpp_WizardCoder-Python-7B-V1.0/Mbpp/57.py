"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    digits.sort(reverse=True)
    result = ""
    for digit in digits:
        result += str(digit)
    return int(result)

print(find_Max_Num([1,2,3])) # Output: 321
print(find_Max_Num([5,4,3,2,1])) # Output: 54321
print(find_Max_Num([9,8,7,6,5,4,3,2,1])) # Output: 987654321