"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""


def extract_string(string_list, size):
    """
    :param string_list: list of strings
    :param size: size of strings to extract
    :return: list of strings
    """
    return [string_list[i] for i in range(len(string_list)) if len(string_list[i]) == size]


if __name__ == '__main__':
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 5))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 3))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 1))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 0))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -1))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -2))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -3))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -4))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -5))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -6))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -7))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -8))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -9))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -10))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -11))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -12))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -13))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -14))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -15))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -16))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -17))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -18))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -19))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -20))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -21))
    print(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], -22))
    print(extract_string(['Python', 'list', 'exer