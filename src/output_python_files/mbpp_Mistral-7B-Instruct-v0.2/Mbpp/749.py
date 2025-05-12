"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""
def sort_numeric_strings(numbers):
    """
    :param numbers: list of strings
    :return: sorted list of strings
    """
    return sorted(numbers, key=lambda x: int(x))

assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10', '101', '100A']
assert sort_numeric_strings( ['10','11','100B','101'])==['10', '101', '100B']
assert sort_numeric_strings( ['10','11','100','101'])==['10', '101', '100']
assert sort_numeric_strings( ['10','11','100A','101'])==['10',