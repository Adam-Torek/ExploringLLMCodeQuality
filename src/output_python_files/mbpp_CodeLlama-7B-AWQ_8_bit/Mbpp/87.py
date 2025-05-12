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
    :return: dictionary
    """
    result = dict1.copy()
    result.update(dict2)
    result.update(dict3)
    return result


if __name__ == '__main__':
    print("Example:")
    print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
    print("Coding complete?