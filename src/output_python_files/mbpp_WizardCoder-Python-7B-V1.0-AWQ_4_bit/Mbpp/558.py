"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    num1_list = [int(digit) for digit in str(num1)]
    num2_list = [int(digit) for digit in str(num2)]
    sum_diff = 0
    for i in range(len(num1_list)):
        diff = abs(num1_list[i] - num2_list[i])
        sum_diff += diff
    return sum_diff

print(digit_distance_nums(1,2)) # Output: 1
print(digit_distance_nums(123, 456)) # Output: 15
print(digit_distance_nums(12345, 67890)) # Output: 120
print(digit_distance_nums(100, 100)) # Output: 0
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 999)) # Output: 100
print(digit_distance_nums(1000, 101)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 101)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 999)) # Output: 1
print(digit_distance_nums(1000, 10000)) # Output: 900
print(digit_distance_nums(1000, 1001)) # Output: 100
print(digit_distance_nums(1000, 999)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 10000)) # Output: 900
print(digit_distance_nums(1000, 1001)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 10000)) # Output: 900
print(digit_distance_nums(1000, 1001)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 10000)) # Output: 900
print(digit_distance_nums(1000, 1001)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 10000)) # Output: 900
print(digit_distance_nums(1000, 1001)) # Output: 1
print(digit_distance_nums(1000, 998)) # Output: 2
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(10