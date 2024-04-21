"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""
def insert_element(lst, elem):
    """
    Takes in a list and an element, and returns a new list with the element inserted before each element in the original list.
    """
    return [elem] + lst

assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']</s>