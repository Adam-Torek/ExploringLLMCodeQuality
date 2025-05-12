"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""

def check_type(tuple_data):
    """
    :param tuple_data: tuple
    :return: True if all the elements in tuple have same data type or False
    """
    data_type = tuple_data[0]
    for i in range(1, len(tuple_data)):
        if type(tuple_data[i]) != data_type:
            return False
    return True