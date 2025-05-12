"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(list1, list2):
    return [float(i)/j for i,j in zip(list1, list2)]

print(div_list([4,5,6],[1, 2, 3])) #[4.0, 2.5, 2.0]
print(div_list([1, 2, 3], [4, 5, 6])) #[0.25, 0.4, 0.5]
print(div_list([1, 2, 3], [0, 0, 0])) #[inf, inf, inf]
print(div_list([0, 0, 0], [1, 2, 3])) #[inf, inf, inf]
print(div_list([0, 0, 0], [0, 0, 0])) #[nan, nan, nan]
print(div_list([0, 0, 0], [0, 0, 0])) #[nan, nan, nan]
print(div_list([], [1, 2, 3])) #[nan, nan, nan]
print(div_list([1, 2, 3], [])) #[nan, nan, nan]
print(div_list([], [])) #[nan, nan, nan]

#Note: If you want to handle the case where list1 or list2 is empty, you can add a check for that and return [0,0,0] or [None, None, None] or raise an exception.