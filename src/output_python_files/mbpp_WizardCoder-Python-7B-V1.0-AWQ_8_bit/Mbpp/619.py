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

print(move_num('I1love143you55three3000thousand')) # Iloveyouthreethousand114353000
print(move_num('I1love143you55three3000thousand123')) # Iloveyouthousand123114353000
print(move_num('123456789')) # 89456732
print(move_num('')) # ''
print(move_num('abc')) # abc
print(move_num('123abc456')) # abc123456
print(move_num('123abc456def')) # abc123456def
print(move_num('123abc456def123')) # abc123def456123
print(move_num('123abc456def123456')) # abc123def456123456
print(move_num('123abc456def123456789')) # abc123def456789123456
print(move_num('123abc456def1234567890')) # abc123def4567890123456
print(move_num('123abc456def1234567890123456789')) # abc123def4567890123456789
print(move_num('123abc456def12345678901234567890')) # abc123def45678901234567890123456
print(move_num('123abc456def12345678901234567890123456789')) # abc123def45678901234567890123456789
print(move_num('123abc456def123456789012345678901234567890')) # abc123def456789012345678901234567890123456
print(move_num('123abc456def123456789012345678901234567890123456789')) # abc123def456789012345678901234567890123456789
print(move_num('123abc456def1234567890123456789012345678901234567890123456789')) # abc123def4567890123456789012345678901234567890123456789
print(move_num('123abc456def1234567890123456