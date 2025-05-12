"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    digits.sort(reverse=True)
    num = ""
    for i in digits:
        num += str(i)
    return int(num)

print(find_Max_Num([1,2,3])) # Output: 321
print(find_Max_Num([5, 5, 5, 5, 5])) # Output: 55555
print(find_Max_Num([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) # Output: 999999999999
print(find_Max_Num([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 987654321

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Efficient Solution
def find_Max_Num_eff(digits):
    digits.sort(reverse=True)
    num = 0
    for i in digits:
        num = num*10 + i
    return num

print(find_Max_Num_eff([1,2,3])) # Output: 321
print(find_Max_Num_eff([5, 5, 5, 5, 5])) # Output: 55555
print(find_Max_Num_eff([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) # Output: 99999999999
print(find_Max_Num_eff([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 987654321

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another Efficient Solution
def find_Max_Num_eff2(digits):
    digits.sort(reverse=True)
    num = 0
    for i in digits:
        num = num*10 + i
    return num

print(find_Max_Num_eff2([1,2,3])) # Output: 321
print(find_Max_Num_eff2([5, 5, 5, 5, 5])) # Output: 55555
print(find_Max_Num_eff2([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) # Output: 99999999999
print(find_Max_Num_eff2([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 987654321

# Time Complexity: O(n)
# Space Complexity: O(1)

# Another Efficient Solution
def find_Max_Num_eff3(digits):
    digits.sort(reverse=True)
    return int("".join(map(str, digits)))

print(find_Max_Num_eff3([1,2,3])) # Output: 321
print(find_Max_Num_eff3([5, 5, 5, 5, 5])) # Output: 55555
print(find_Max_Num_eff3([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])) # Output: 99999999999
print(find_Max_Num_eff3([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 987654321

# Time Complexity: O(n