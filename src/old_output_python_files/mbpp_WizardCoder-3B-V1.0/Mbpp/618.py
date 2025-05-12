"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(list1, list2):
    return [x/y for x,y in zip(list1, list2)]

# Test the function
print(div_list([4,5,6],[1, 2, 3]))<|endoftext|>