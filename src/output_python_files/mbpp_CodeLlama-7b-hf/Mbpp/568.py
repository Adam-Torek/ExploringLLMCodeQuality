"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""

def empty_list(n):
    """
    Create a list of N empty dictionaries.
    """
    return [{}] * n


def test_empty_list():
    assert empty_list(5) == [{}, {}, {}, {}, {}]


if __name__ == '__main__':
    test_empty_list()