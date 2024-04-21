"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""

def toggle_middle_bits(num):
    """
    Toggle all bits except the first and the last bit
    """
    # First bit is 1, last bit is 1, all other bits are 0
    mask = 0b1111111011111110
    # Shift the mask to the right by the number of bits
    # to get to the position of the number
    mask = mask >> (len(bin(num)[0:len(bin(num)[0:len(bin(num)[0:len(bin(num))-2]))]))
    # XOR the number with the mask
    return num ^ mask

if __name__ == "__main__":
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(15) == 9
    assert toggle_middle_bits(1) == 1
    assert toggle_middle_bits(16) == 14
    assert toggle_middle_bits(14) == 16
    print("All tests passed")</s>