"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""


def merge_dictionaries_three(dict1, dict2, dict3):
    """
    Merge three dictionaries into a single dictionary.
    :param dict1: dictionary
    :param dict2: dictionary
    :param dict3: dictionary
    :return: merged dictionary
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict


if __name__ == '__main__':
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"},
                                   {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({