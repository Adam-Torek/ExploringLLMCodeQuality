"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(nested_list):
    """
    >>> flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/easy/14_longest_common_prefix.py
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

assert longest_common_prefix(["flower","flow","flight"])=="fl"
assert longest_common_prefix(["dog","racecar","car"])==""
"""

def longest_common_prefix(strs):
    """
    >>> longest_common_prefix(["flower","flow","flight"])
    'fl'
    >>> longest_common_prefix(["dog","racecar","car"])
    ''
    """
    if not strs:
        return ""
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix)!= 0:
            prefix = prefix[:-1]
    return prefix

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/easy/13_roman_to_integer.py
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

assert roman_to_integer("III") == 3
assert roman_to_integer("IV") == 4
assert roman_to_integer("IX") == 9
assert roman_to_integer("LVIII") == 58
assert roman_to_integer("MCMXCIV") == 1994
"""

def roman_to_integer(s):
    """
    >>> roman_to_integer("III")
    3
    >>> roman_to_integer("IV")
    4
    >>> roman_to_integer("IX")
    9
    >>> roman_to_integer("LVIII")
    58
    >>> roman_to_integer("MCMXCIV")
    1994
    """
    roman_to_integer_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        if i > 0 and roman_to_integer_map[s[i]] > roman_to_integer_map[s[i - 1]]:
            result += roman_to_integer_map[s[i]] - 2 * roman_to_integer_map[s[i - 1]]
        else:
            result += roman_to_integer_map[s[i]]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/leetcode/easy/11_container_with_most_water.py
"""
Given n non-negative integers a1, a2,..., an, where each represents a point at coordinate (i, ai