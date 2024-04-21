"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string, n):
    binary_string = binary_string.zfill(len(binary_string))
    count = 0
    for i in range(n):
        binary_string = binary_string[1:] + binary_string[0]
        if binary_string.count('1') % 2!= 0:
            count += 1
    return count

# Test the function
assert odd_Equivalent("011001",6) == 3<|endoftext|>