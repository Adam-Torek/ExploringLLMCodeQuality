"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] - list2[i])
    return result

print(sub_list([1, 2, 3],[4,5,6])) # Output: [-3, -3, -3]
print(sub_list([1, 2, 3],[4,5,6,7])) # Output: [-3, -3, -4]
print(sub_list([1, 2],[4,5,6])) # Output: [-3, -3]
print(sub_list([1, 2],[4,5])) # Output: [-3]
print(sub_list([1],[4,5,6])) # Output: []
print(sub_list([],[4,5,6]) # Output: []