"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""

def move_num(s):
    """
    Move all the numbers to the end of the given string.
    """
    return ''.join(filter(str.isalpha, s)) + s