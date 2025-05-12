"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2)) # [5,6,52,36,12,10]
print(split_Arr([1,2,3,4,5,6,7,8,9],4)) # [5,6,7,8,9,1,2,3,4]
print(split_Arr([1,2,3,4,5,6,7,8,9],1)) # [2,3,4,5,6,7,8,9,1]
print(split_Arr([1,2,3,4,5,6,7,8,9],7)) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([1,2,3,4,5,6,7,8,9],0)) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([1,2,3,4,5,6,7,8,9],8)) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([1,2,3,4,5,6,7,8,9],-1)) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([],2)) # []
print(split_Arr([1],2)) # [1]
print(split_Arr([1,2],2)) # [2,1]
print(split_Arr([1,2,3,4,5,6,7,8,9],10) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([1,2,3,4,5,6,7,8,9],100) # [1,2,3,4,5,6,7,8,9]
print(split_Arr([1,2,3,4,5,6,7,8,9],-100) # [1,2,3,4,5,6,7,8,9]