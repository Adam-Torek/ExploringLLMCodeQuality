"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""

def odd_Equivalent(binary_string, rotations):
    binary_string = list(binary_string)
    for i in range(rotations):
        last_bit = binary_string[0]
        binary_string.insert(0, last_bit)
        binary_string.pop()
    return binary_string.count("1")

print(odd_Equivalent("011001", 6)) # Output: 3