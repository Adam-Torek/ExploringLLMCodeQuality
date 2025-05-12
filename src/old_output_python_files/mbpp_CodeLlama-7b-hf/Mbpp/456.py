"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""


def reverse_string_list(string_list):
    """
    :param string_list: list of strings
    :return: list of reversed strings
    """
    return [string[::-1] for string in string_list]


if __name__ == '__main__':
    print(reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))
    print(reverse_string_list(['R', 'G', 'B', 'W', 'K', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '']))