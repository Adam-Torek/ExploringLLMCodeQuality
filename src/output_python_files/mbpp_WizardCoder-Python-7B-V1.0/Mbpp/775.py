"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""
def odd_position(lst):
    for i in range(1,len(lst),2):
        if lst[i]%2==0:
            return False
    return True

print(odd_position([2,1,4,3,6,7,6,3])) # True
print(odd_position([2,1,4,3,6,8,3])) # False
print(odd_position([1,2,3,4,5,6,7])) # False
print(odd_position([1,3,5,7,9,11])) # True
print(odd_position([1,2,4,6,8,10])) # False
print(odd_position([1,3,5,7,9]))   # True
print(odd_position([1,2,4,6,8]))  # False
print(odd_position([1,3,5,7]))   # True
print(odd_position([1,2,4,6]))  # False
print(odd_position([1,3,5]))    # True
print(odd_position([1,2]))     # False
print(odd_position([]))       # True
print(odd_position([1]))      # False
print(odd_position([1,2,3,4,5,6,7,8,9,10])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # False
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])) # True
print(odd_position([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17