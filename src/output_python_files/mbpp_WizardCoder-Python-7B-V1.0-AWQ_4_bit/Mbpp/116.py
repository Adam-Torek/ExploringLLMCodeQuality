"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""

def tuple_to_int(tup):
    return int(''.join(str(i) for i in tup))

print(tuple_to_int((1,2,3))==123) # True
print(tuple_to_int((1,0,2,3))==1023) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9))==123456789) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,10)==12345678910) # True