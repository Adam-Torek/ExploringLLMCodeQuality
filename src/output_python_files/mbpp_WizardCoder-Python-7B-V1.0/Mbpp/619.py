"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(string):
    nums = []
    non_nums = []
    for char in string:
        if char.isdigit():
            nums.append(char)
        else:
            non_nums.append(char)
    return ''.join(non_nums) + ''.join(nums)

# Test cases
print(move_num('I1love143you55three3000thousand')) # Output: Iloveyouthreethousand1143553000
print(move_num('a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q17r18s19t20u21v22w23x24y25z26')) # Output: abcdefghijklmnopqrstuvwxyz1011121314151617181920212223242526
print(move_num('1234567890')) # Output: 1234567890
print(move_num('')) # Output: