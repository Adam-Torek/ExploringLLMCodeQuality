"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""

def is_sublist(list1, list2):
    if len(list1) > len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
            else:
                return True

print(is_sublist([2,4,3,5,7],[3,7]))
print(is_sublist([2,4,3,5,7],[3,7,5]))
print(is_sublist([2,4,3,5,7],[3,7,5,7]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3,5]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3,5,7]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3,5,7,2]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3,5,7,2,4]))
print(is_sublist([2,4,3,5,7],[3,7,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3,5,7,2,4,3]))
print(is_sublist([2,4,3,5,7],[3,7,