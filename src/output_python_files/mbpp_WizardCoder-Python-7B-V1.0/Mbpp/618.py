"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(list1, list2):
    return [float(i)/j for i,j in zip(list1, list2)]

print(div_list([4,5,6],[1, 2, 3])) # Output: [4.0, 2.5, 2.0]
print(div_list([10, 20, 30], [5, 10, 15])) # Output: [2.0, 2.0, 2.0]
print(div_list([1, 2, 3], [4, 5, 6])) # Output: [0.25, 0.4, 0.5]
print(div_list([0, 0, 0], [1, 1, 1])) # Output: [0.0, 0.0, 0.0]
print(div_list([1, 2, 3], [0, 0, 0])) # Output: [inf, inf, inf]
print(div_list([], [1, 2, 3])) # Output: []
print(div_list([1, 2, 3], [])) # Output: []
print(div_list([], [])) # Output: []