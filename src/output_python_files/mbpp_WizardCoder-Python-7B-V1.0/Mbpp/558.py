"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    sum = 0
    for i in range(len(num1_str)):
        sum += abs(int(num1_str[i]) - int(num2_str[i]))
    return sum

print(digit_distance_nums(1,2)) # Output: 1
print(digit_distance_nums(123, 456)) # Output: 15
print(digit_distance_nums(12345, 67890)) # Output: 40
print(digit_distance_nums(123456, 789012)) # Output: 40
print(digit_distance_nums(123456789, 987654321)) # Output: 40
print(digit_distance_nums(1234567890, 9876543210)) # Output: 40
print(digit_distance_nums(12345678901234567890, 98765432109876543210)) # Output: 40
print(digit_distance_nums(123456789012345678901234567890, 987654321098765432109876543210)) # Output: 40

# Time Complexity: O(n)
# Space Complexity: O(1)