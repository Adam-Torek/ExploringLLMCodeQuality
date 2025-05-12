"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""
def add_string(lst, format_string):
    """
    :param lst: list of elements
    :param format_string: string with placeholders
    :return: list of strings with placeholders filled in
    """
    return [format_string.format(i) for i in lst]

assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']