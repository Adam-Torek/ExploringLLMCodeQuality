"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""


def merge_dictionaries_three(dict1, dict2, dict3):
    """
    :param dict1: dictionary
    :param dict2: dictionary
    :param dict3: dictionary
    :return: dictionary
    """
    dict_final = {}
    for key, value in dict1.items():
        dict_final[key] = value
    for key, value in dict2.items():
        dict_final[key] = value
    for key, value in dict3.items():
        dict_final[key] = value
    return dict_final


if __name__ == '__main__':
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"},
                                   {"O": "Orange", "W": "White", "B": "Black"}))
    print(merge_dictionaries_three({"R": "Red", "B": "Black", "P": "P