"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(t1, t2):
    """
    >>> find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10))
    (3, 6, 7, 10)
    """
    return tuple(set(t1) ^ set(t2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_practice/python_practice_2017/python_practice_2017_03/python_practice_2017_03_19.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string in a list of strings.
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
"""

def longest_common_prefix(strs):
    """
    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'
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
/python/python_practice/python_practice_2017/python_practice_2017_03/python_practice_2017_03_14.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string in a list of strings.
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
"""

def longest_common_prefix(strs):
    """
    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'
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
/python/python_practice/python_practice_2017/python_practice_2017_03/python_practice_2017_03_15.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string in a list of strings.
assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
"""

def longest_common_prefix(strs):
    """
    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'
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
/python/python_practice/python_practice_2017/python_practice_2017_03/python_practice_2017_03_16.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string in a list of strings.
assert longest_common_prefix(["flower", "flow", "flight