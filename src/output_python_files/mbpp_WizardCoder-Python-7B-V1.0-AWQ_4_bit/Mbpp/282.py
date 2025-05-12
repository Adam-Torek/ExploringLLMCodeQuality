"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""

def sub_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists must be of same length"
    else:
        result = []
        for i in range(len(list1)):
            result.append(list1[i] - list2[i])
        return result

print(sub_list([1, 2, 3],[4,5,6])) # [-3, -3, -3]
print(sub_list([1, 2, 3],[4,5,6,7])) # "Lists must be of same length"
print(sub_list([1, 2],[4,5,6])) # "Lists must be of same length"
print(sub_list([1, 2, 3],[4,5])) # "Lists must be of same length"

# Test cases
# print(sub_list([1, 2, 3],[4,5,6])) # [-3, -3, -3]
# print(sub_list([1, 2, 3],[4,5,6,7])) # "Lists must be of same length"
# print(sub_list([1, 2],[4,5,6])) # "Lists must be of same length"
# print(sub_list([1, 2, 3],[4,5]) # "Lists must be of same length"