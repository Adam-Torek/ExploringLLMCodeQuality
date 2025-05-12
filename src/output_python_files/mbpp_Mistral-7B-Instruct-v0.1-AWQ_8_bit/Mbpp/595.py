"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_Swaps(num1, num2):
    count = 0
    while num1 != num2:
        if num1[0] == num2[0]:
            num1 = num1[1:]
            num2 = num2[1:]
        else:
            count += 1
    return count

assert min_Swaps("1101","1110") == 1