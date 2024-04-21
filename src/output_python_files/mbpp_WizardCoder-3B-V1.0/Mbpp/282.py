"""
Write a function to subtract two lists element-wise.
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
"""
def sub_list(list1, list2):
    return [x-y for x,y in zip(list1, list2)]

assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]<|endoftext|>