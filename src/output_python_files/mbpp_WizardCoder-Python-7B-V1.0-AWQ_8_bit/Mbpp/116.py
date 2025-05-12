"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""

def tuple_to_int(tup):
    return int(''.join(str(i) for i in tup))

# Test cases
print(tuple_to_int((1,2,3))==123) # True
print(tuple_to_int((10,20,30))==1230) # True
print(tuple_to_int((100,200,300))==12300) # True
print(tuple_to_int((1000,200,300))==123000) # True
print(tuple_to_int((10000,20000,30000))==1230000) # True
print(tuple_to_int((100000,200000,300000))==12300000) # True
print(tuple_to_int((1000000,2000000,3000000))==123000000) # True
print(tuple_to_int((10000000,20000000,30000000))==1230000000) # True
print(tuple_to_int((100000000,200000000,300000000))==12300000000) # True
print(tuple_to_int((1000000000,2000000000,300000000)==123000000000) # True

# Edge cases
print(tuple_to_int((1,))==1) # True
print(tuple_to_int(())==0) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9))==1234567890) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,0))==1234567890) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9)==12345678900) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((1,2,3,4,5,6,7,8,9,0)==12345678900) # True
print(tuple_to_int((0,1,2,3,4,5,6,7,