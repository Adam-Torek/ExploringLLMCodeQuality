"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(lst, element):
    count = 0
    for sublist in lst:
        if element in sublist:
            count += 1
    return count

print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)) # Output: 3
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],7) # Output: 2
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],5) # Output: 1
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],15) # Output: 1
print(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],2) # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(1)