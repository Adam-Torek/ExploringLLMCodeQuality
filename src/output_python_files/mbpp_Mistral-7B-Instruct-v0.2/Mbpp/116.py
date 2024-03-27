"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
def tuple_to_int(numbers):
    """
    Converts a given tuple of positive integers into a single integer.
    :param numbers: tuple of positive integers
    :return: single integer
    """
    return int(''.join(map(str, numbers)))

assert tuple_to_int((1,2,3))==123
assert tuple_to_int((4,5,6))==2160
assert tuple_to_int((1,1,1,1,1,1,1,1,1,1))==102345678910
assert tuple_to_int((1,2,3,4,5,6,7,8,9,0))==123456789011
assert tuple_to_int((1,2,3,4,5,6,7,8,9,10))==12345678901112
assert tuple_to_int((1,2,3,4,5,6,7,8,9,11))==1234567890111213
assert tuple_to_int((1,2,3,4,5,6,7,8,9,12))==123456789011121314
assert tuple_to_int((1,2,3,4,5,6,7,8,9,13))==12345678901112131415
assert tuple_to_int((1,2,3,4,5,6,7,8,9,14))==1234567890111213141516
assert tuple_to_int((1,2,3,4,5,6,7,8,9,15))==123456789011121314151617
assert tuple_to_int((1,2,3,4,5,6,7,8,9,16))==12345678901112131415161718
assert tuple_to_int((1,2,3,4,5,6,7,8,9,17))==1234567890111213141516171819
assert tuple_to_int((1,2,3,4,5,6,7,8,9,18))==123456789011121314151617181920
assert tuple_to_int((1,2,3,4,5,6,7,8,9,19))==12345678901112131415161718192021
assert tuple_to_int((1,2,3,4,5,6,7,8,9,20))==1234567890111213141516171819202122
assert tuple_to_int((1,2,3,4,5,6,7,8,9,21))==123456789011121314151617181920212223
assert tuple_to_int((1,2,3,4,5,6,7,8,9,22))==12345678901112131415161718192021222324
assert tuple_to_int((1,2,3,4,5,6,7,8,9,23))==1234567890111213141516171819202122232425