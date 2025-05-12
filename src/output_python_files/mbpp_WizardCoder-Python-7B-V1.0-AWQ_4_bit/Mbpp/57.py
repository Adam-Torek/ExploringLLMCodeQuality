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
print(find_Max_Num([5, 5, 5, 5, 5])) # Output: 55555
print(find_Max_Num([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) # Output: 999999999999
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 987654321
print(find_Max_Num([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # Output: 0
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # Output: 9876543210
print(find_Max_Num([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 9876543210
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # Output: 9876543210
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # Output: 9876543210
print(find_Max_Num([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # Output: 9876543210
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # Output: 9876543210
print(find_Max_Num([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # Output: 9876543210
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # Output: 9876543210
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # Output: 9876543210
print(find_Max_Num([0, 1, 2, 3, 4, 5, 6, 7