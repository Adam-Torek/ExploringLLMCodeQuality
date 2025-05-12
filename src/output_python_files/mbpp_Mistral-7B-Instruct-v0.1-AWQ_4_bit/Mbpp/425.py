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


# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],2)==2
# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],3)==1
# assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],4)==0