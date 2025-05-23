"""
Write a function to sort a given list of strings of numbers numerically. https://www.geeksforgeeks.org/python-sort-numeric-strings-in-a-list/
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""


def sort_numeric_strings(strings):
    """
    Sorts a list of strings of numbers numerically.
    :param strings: list of strings of numbers
    :return: list of strings of numbers sorted numerically
    """
    return sorted(strings, key=lambda x: int(x))


if __name__ == '__main__':
    print(sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']))
    print(sort_numeric_strings(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
    print(sort_numeric_strings(['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '3', '4', '5',
                                 '6', '7', '8', '9']))
    print(sort_numeric_strings(['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '3', '4', '5',
                                 '6', '7', '8', '9', '100', '101', '102', '103', '104', '105', '106', '107', '108',
                                 '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120',
                                 '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132',
                                 '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144',
                                 '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156',
                                 '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168',
                                 '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180',
                                 '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192',
                                 '193', '194', '195', '196', '197', '198', '199', '2', '3', '4', '5', '6', '7', '8',
                                 '9']))
    print(sort_numeric_strings(['1', '10', '11', '12', '