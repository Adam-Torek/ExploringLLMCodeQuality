def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert string to lower case
    string = string.lower()

    # Create an empty set to store unique characters
    unique_chars = set()

    # Iterate over each character in the string
    for char in string:
        # If character is not in the set, add it
        if char not in unique_chars:
            unique_chars.add(char)

    # Return the length of the set (i.e. number of unique characters)
    return len(unique_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))