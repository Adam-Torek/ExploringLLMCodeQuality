"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(lst, elem):
    count = 0
    for sublist in lst:
        if elem in sublist:
            count += 1
    return count

# Test the function
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) # Output: 3<|endoftext|>