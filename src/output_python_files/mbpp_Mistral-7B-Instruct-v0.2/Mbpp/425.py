"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""
def count_element_in_list(lst, element):
    """
    :param lst: list of lists
    :param element: element to count
    :return: number of sublists containing the element
    """
    return sum(1 for sublist in lst if element in sublist)

assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],7)==1
assert count_element_in_list([],1)==0
assert count_element_in_list([],7)==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0
assert count_element_in_list([],[])==0