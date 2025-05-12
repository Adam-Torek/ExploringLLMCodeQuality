"""
Write a function to apply a given format string to all of the elements in a list.
assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']
"""

def add_string(lst, format_string):
    """
    Apply a given format string to all of the elements in a list.
    """
    return [format_string.format(i) for i in lst]


if __name__ == '__main__':
    print(add_string([1,2,3,4],'temp{0}'))