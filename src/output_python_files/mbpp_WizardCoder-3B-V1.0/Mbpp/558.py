"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(num1, num2):
    # Convert the numbers to strings
    str1 = str(num1)
    str2 = str(num2)

    # Initialize the sum of differences
    diff_sum = 0

    # Loop through each digit in the strings
    for i in range(len(str1)):
        # Calculate the difference between the digits
        diff = abs(int(str1[i]) - int(str2[i]))

        # Add the difference to the sum
        diff_sum += diff

    return diff_sum

# Test the function with the given example
assert digit_distance_nums(1,2) == 1<|endoftext|>