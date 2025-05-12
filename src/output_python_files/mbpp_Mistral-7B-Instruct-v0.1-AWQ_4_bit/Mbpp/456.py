"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
def reverse_string_list(lst):
    """
    This function takes a list of string values and returns a new list of string values
    where each string is reversed.
    """
    reversed_lst = []
    for string in lst:
        reversed_string = string[::-1]
        reversed_lst.append(reversed_string)
    return reversed_lst

# Test the function
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']