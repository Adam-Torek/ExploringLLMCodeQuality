"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""

def tuple_to_int(tup):
    return int(''.join(str(i) for i in tup))

# Test cases
print(tuple_to_int((1,2,3))==123) # True
print(tuple_to_int((12,34,56))==123456) # True
print(tuple_to_int((123,456,789))==123456789) # True
print(tuple_to_int((1000,2000,3000))==1000200300) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9)==123456789) # True