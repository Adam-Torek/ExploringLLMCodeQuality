"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""

def insert_element(lst, element):
    """
    Insert an element before each element in the list
    """
    return [element] + lst