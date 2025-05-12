def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    shift = shift % len(digits)
    return digits[-shift:] + digits[:-shift]


def circular_shift_list(lst, shift):
    """Circular shift the elements of the list, shift the elements right by shift
    and return the result as a list.
    If shift > length of the list, return the list reversed.
    >>> circular_shift_list([1, 2, 3], 1)
    [2, 3, 1]
    >>> circular_shift_list([1, 2, 3], 2)
    [3, 1, 2]
    """
    shift = shift % len(lst)
    return lst[-shift:] + lst[:-shift]

def circular_shift_string(s, shift):
    """Circular shift the characters of the string, shift the characters right by shift
    and return the result as a string.
    If shift > length of the string, return the string reversed.
    >>> circular_shift_string("abc", 1)
    "bc"
    >>> circular_shift_string("abc", 2)
    "cab"
    """
    shift = shift % len(s)
    return s[-shift:] + s[:-shift]

def circular_shift_dict(d, shift):
    """Circular shift the keys of the dictionary, shift the keys right by shift
    and return the result as a new dictionary.
    If shift > number of keys, return the dictionary reversed.
    >>> circular_shift_dict({"a": 1, "b": 2, "c": 3}, 1)
    {"b": 2, "c": 3, "a": 1}
    >>> circular_shift_dict({"a": 1, "b": 2, "c": 3}, 2)
    {"c": 3, "a": 1, "b": 2}
    """
    shift = shift % len(d)
    keys = list(d.keys())
    keys = circular_shift_list(keys, shift)
    return {k: d[k] for k in keys}

def circular_shift_set(s, shift):
    """Circular shift the elements of the set, shift the elements right by shift
    and return the result as a new set.
    If shift > length of the set, return the set reversed.
    >>> circular_shift_set({1, 2, 3}, 1)
    {2, 3, 1}
    >>> circular_shift_set({1, 2, 3}, 2)
    {3, 1, 2}
    """
    shift = shift % len(s)
    lst = list(s)
    lst = circular_shift_list(lst, shift)
    return set(lst)

def circular_shift_tuple(t, shift):
    """Circular shift the elements of the tuple, shift the elements right by shift
    and return the result as a new tuple.
    If shift > length of the tuple, return the tuple reversed.
    >>> circular_shift_tuple((1, 2, 3), 1)
    (2, 3, 1)
    >>> circular_shift_