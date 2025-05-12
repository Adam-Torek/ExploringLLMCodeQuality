"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""

def min_Swaps(binary1, binary2):
    # Convert binary strings to integers
    num1 = int(binary1, 2)
    num2 = int(binary2, 2)

    # Initialize variables
    count = 0
    carry = 0

    # Iterate through each bit of the binary numbers
    for i in range(32):
        # Calculate the sum of the current bits
        sum = (num1 >> i) & 1 + (num2 >> i) & 1 + carry

        # If the sum is greater than 1, add a swap and set the carry to 1
        if sum > 1:
            count += 1
            carry = 1
        else:
            carry = 0

    # If there is a carry left, add a swap
    if carry == 1:
        count += 1

    return count

# Test the function
assert min_Swaps("1101", "1110") == 1<|endoftext|>