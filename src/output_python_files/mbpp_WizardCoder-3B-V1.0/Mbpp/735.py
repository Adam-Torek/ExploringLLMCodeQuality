"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(num):
    # convert the number to binary string
    binary_str = bin(num)[2:]
    # get the length of the binary string
    length = len(binary_str)
    # get the index of the first and last bits
    first_bit_index = length - 1
    last_bit_index = 0
    # toggle the middle bits
    for i in range(first_bit_index, last_bit_index):
        if binary_str[i] == '0':
            binary_str[i] = '1'
        else:
            binary_str[i] = '0'
    # convert the binary string back to integer
    num = int(binary_str, 2)
    return num

# test the function
print(toggle_middle_bits(9)) # expected output: 15<|endoftext|>