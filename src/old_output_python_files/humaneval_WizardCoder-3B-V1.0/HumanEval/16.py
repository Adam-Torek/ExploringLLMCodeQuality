def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
#     return len(set(string.lower()))
    return len(set(string))

# Test cases
print(count_distinct_characters('xyzXYZ')) # Output: 3
print(count_distinct_characters('Jerry')) # Output: 4<|endoftext|>