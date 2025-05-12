"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""


def extract_string(string_list, size):
    """
    :param string_list: list of strings
    :param size: size of string to extract
    :return: list of strings
    """
    return [string_list[i:i + size] for i in range(len(string_list)) if len(string_list[i:i + size]) == size]


if __name__ == '__main__':
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 10))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 1))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 100))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 0))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -100))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -100000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -100000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -100000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1000000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -100000000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1000000000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000000000000000))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10000000