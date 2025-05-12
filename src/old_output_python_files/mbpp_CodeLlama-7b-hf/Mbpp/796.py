"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""


def return_sum(dictionary):
    """
    :param dictionary: dictionary
    :return: sum of all items in the given dictionary
    """
    return sum(dictionary.values())


if __name__ == '__main__':
    print(return_sum({'a': 100, 'b': 200, 'c': 300}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900, 'j': 1000}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900, 'j': 1000, 'k': 1100}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900, 'j': 1000, 'k': 1100, 'l': 1200}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900, 'j': 1000, 'k': 1100, 'l': 1200, 'm': 1300}))
    print(return_sum({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600, 'g': 700, 'h': 800, 'i': 900, 'j': 1000, 'k': 1100, 'l': 1200, 'm':