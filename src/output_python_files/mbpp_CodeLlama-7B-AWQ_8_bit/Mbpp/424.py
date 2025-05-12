"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""


def extract_rear(tuple_of_strings):
    """
    :param tuple_of_strings: tuple of strings
    :return: list of rear index elements
    """
    return [string[-1] for string in tuple_of_strings]


if __name__ == '__main__':
    print(extract_rear(('Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for',
                        'Mers', 'for', 'Vers')))
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers',