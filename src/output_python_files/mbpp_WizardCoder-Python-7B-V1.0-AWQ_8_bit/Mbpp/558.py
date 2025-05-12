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
print(digit_distance_nums(12345, 67890)) # Output: 120
print(digit_distance_nums(1000, 200)) # Output: 100
print(digit_distance_nums(1000, 1000)) # Output: 0
print(digit_distance_nums(1000, 0)) # Output: 100
print(digit_distance_nums(0, 100)) # Output: 100
print(digit_distance_nums(0, 0)) # Output: 0
print(digit_distance_nums(123456789, 987654321)) # Output: 123456789
print(digit_distance_nums(123456789, 123456789)) # Output: 0
print(digit_distance_nums(123456789, 123456788)) # Output: 1
print(digit_distance_nums(123456789, 123456787)) # Output: 2
print(digit_distance_nums(123456789, 123456786)) # Output: 3
print(digit_distance_nums(123456789, 123456785)) # Output: 4
print(digit_distance_nums(123456789, 123456784)) # Output: 5
print(digit_distance_nums(123456789, 123456783)) # Output: 6
print(digit_distance_nums(123456789, 123456782)) # Output: 7
print(digit_distance_nums(123456789, 123456781)) # Output: 8
print(digit_distance_nums(123456789, 123456780)) # Output: 9
print(digit_distance_nums(123456789, 123456779)) # Output: 10
print(digit_distance_nums(123456789, 123456778)) # Output: 11
print(digit_distance_nums(123456789, 123456777)) # Output: 12
print(digit_distance_nums(123456789, 123456776)) # Output: 13
print(digit_distance_nums(123456789, 123456775)) # Output: 14
print(digit_distance_nums(123456789, 123456774)) # Output: 15
print(digit_distance_nums(123456789, 123456773)) # Output: 16
print(digit_distance_nums(123456789, 123456772)) # Output: