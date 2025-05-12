"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""

def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

print(common_element([1,2,3,4,5], [5,6,7,8,9]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(common_element([1,2,3,4,5], [5,6,7,8,9,10,11,12,13,14,15,16