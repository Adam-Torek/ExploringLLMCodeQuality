"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""


def extract_rear(tuple_):
    """
    :param tuple_: tuple of strings
    :return: list of rear index elements of each string in the given tuple
    """
    return [tuple_[i][-1] for i in range(len(tuple_))]


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
    print(extract_rear(('Mers', 'for', 'Vers', 'for', 'Mers', 'for', 'Vers', 'for', 'Mers', '